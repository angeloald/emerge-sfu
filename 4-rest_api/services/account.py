"""This file contains our business logic"""

from services import db


def create_account(name):
    db.create_user(name)


def get_account(name):
    return db.read_account(name)


def deposit(name, amount):
    db.add_balance(name, amount)


def withdraw(name, amount):
    db.add_balance(name, -1 * amount)


def get_balance(name):
    user = db.search(Account.name == name)
    if user == []:
        return None
    return user[0]["balance"]

def add_expense(name, expense_name, expens_amount):
    user = db.search(A)
