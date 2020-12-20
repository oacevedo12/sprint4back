from pydantic import BaseModel

class CustomerPayment(BaseModel):
    id_customer: int
    name: str

class CustomerOut(BaseModel):
    id_customer: int
    name: str
    invoice: int
    payment: bool

