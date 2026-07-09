from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: int
    name: str
    email: str
    department: str
    position: str
    hire_date: str
    salary: int
    active: bool
