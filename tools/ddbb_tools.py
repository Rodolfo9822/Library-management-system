from functions import account_valid
import json
from pathlib import Path


def employee_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/employee_data.json"


def member_path():
    return ""


def account_exist(employee, user_email, user_pass):
    email = employee["email"]
    password = employee["password"]
    if email == user_email and password == user_pass:
        return True, employee


def to_get_data(path, user_email, user_pass):
    file = Path(path).read_text(encoding="utf-8")
    for employee in json.loads(file):
        exist = account_exist(employee, user_email, user_pass)
    return exist


def sign_in(message):
    print(message)
    email = input("Write your email: ")
    password = input("Write your password: ")
    account = account_valid(email)
    if account:
        data = to_get_data(employee_path(), email, password)
        return data
    else:
        print("Invalid email, please check out your email")
        return False, ""
