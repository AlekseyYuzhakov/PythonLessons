import typing
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: typing.Optional[bool] = None


class User(BaseModel):
    name: str
    Full_name: typing.Optional[str] = None


class Order(BaseModel):
    items: List[Item]
    user: User
