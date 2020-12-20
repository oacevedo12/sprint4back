from typing import Dict
from pydantic import BaseModel

class CustomerInDB(BaseModel):
    id_customer : int
    name: str
    address: str
    invoice: int
    payment: bool

database_customers = Dict[str, CustomerInDB]

database_customers = {
    "Multidimensionales": CustomerInDB(**{"id_customer": 1000,
                                        "name": "Multidimensionales",
                                        "address": "Bogotá",
                                        "invoice" : 125,
                                        "payment": True
                                        }),
    
    "Fepco": CustomerInDB(**{"id_customer": 1001,
                            "name": "Fepco",
                            "address": "Bogotá",
                            "invoice" : 131,
                            "payment": False
                                        }),

    "Indumil": CustomerInDB(**{"id_customer" : 1002,
                               "name": "Indumil",
                               "address": "Soacha",
                               "invoice" : 186,
                               "payment": False
                                        })
                    }

def get_customer(name:str):
    if name in database_customers.keys():
        return database_customers[name]
    else:
        return None


def update_customer(customer_in_db: CustomerInDB):
    database_customers[customer_in_db.username] = customer_in_db
    return customer_in_db