from db.employee_db import EmployeeInDB
from db.employee_db import update_employee, get_employee, display_all
from models.employee_models import EmployeeLogin, EmployeeLogout, EmployeeTask
from models.customer_model import CustomerPayment
from db.customers_db import get_customer, update_customer
from db.customers_db import CustomerInDB
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict

api = FastAPI(
    title="Sprints 4 y 5",
    description="APIs para módulos de empleados y clientes",
    version="0.0.1.1",
)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

api.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Login de empleado método post
@api.post("/employee/auth/")
async def auth_employee(employee_login: EmployeeLogin):
    employee_in_db = get_employee(employee_login.username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El empleado no existe")

    if employee_in_db.password != employee_login.password:
        return {"Autenticado": False}
    else:
        employee_in_db.logged_in = True
        update_employee(employee_in_db)
        return {"Autenticado": True}

#Consultar empleado
@api.get("/employee/data/{username}")
async def get_employee_data(username: str):
    employee_in_db = get_employee(username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    return employee_in_db

#Logout de empleado
@api.get("/employee/signout/{username}")
async def signout_employee(username: str):
    employee_in_db = get_employee(username)

    if employee_in_db is None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    employee_in_db.logged_in = False

    update_employee(employee_in_db)

    return {"Cerrar Sesión": True}


#Actualizar tarea empleado
@api.put("/employee/task/")
async def assign_task(employee_task: EmployeeTask):
    employee_in_db = get_employee(employee_task.username)

    if employee_in_db == None:
        raise HTTPException(status_code=404, detail="El empleado no existe")

    employee_in_db.task = employee_task.task
    update_employee(employee_in_db)

    return employee_in_db

#Mostrar todos los empleados
@api.get("/employees/", response_model=Dict[str, EmployeeInDB])
async def find_all_employees():
    employee_db = display_all()
    return employee_db

#API´s clientes

@api.get("/customer/data/{name}")
async def get_customer_data(name: str):

    customer_in_db = get_customer(name)

    if customer_in_db == None:
        raise HTTPException(status_code=404, detail="El cliente no existe")

    return  customer_in_db


@api.put("/customer/payment/")
async def customer_payment(customer_pay: CustomerPayment):

    customer_pay_in_db = get_customer(customer_pay.payment)

    if customer_pay_in_db == False:
        return "El cliente no ha pagado"
    
    else:
        customer_pay_in_db = not customer_pay.payment
        update_customer(customer_pay.payment)

        return  update_customer

