import os
try:
    os.remove("db.json")
except OSError:
    pass


import services.account as account
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


class Account(BaseModel):
    name: str
    amount: Optional[float] = 0


@app.post("/account/create")
def create_account(user_account: Account):
    account.create_account(user_account.name)
    return account.get_account(user_account.name)
    return user_account.name


@app.get("/account/{user_account}")
def read_account(user_account: str):
    return account.get_account(user_account)


@app.put("/account/deposit")
def deposit_to_account(user_account: Account):
    account.deposit(user_account.name, user_account.amount)
    return account.get_account(user_account.name)
