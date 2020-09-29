"""This file interacts with our toy database."""

from tinydb import TinyDB, Query
from tinydb.operations import add
import time

db = TinyDB('db.json')
Account = Query()


def create_user(name):
    db.insert({"name": name, "balance": 0, "expenses": []})


def read_account(name):
    return db.search(Account.name == name)


def add_balance(name, amount):
    db.update(add("balance", amount), Account.name == name)


def add_expense(name, expense_name, expense_amount):
    def create_expense():
        def transform(doc):
            doc["expenses"].append(
                {"expense": expense_name, "amount": expense_amount, "time": int(time.time())})
            doc["balance"] -= expense_amount
        return transform
    db.update(create_expense(), Account.name == name)
