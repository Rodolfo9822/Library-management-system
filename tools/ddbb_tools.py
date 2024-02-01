from functions import account_valid
from messages import message_to_employee
import json
from pathlib import Path


def employee_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/employee_data.json"


def member_path():
    return ""


def to_get_data(path):
    file = Path(path).read_text(encoding="utf-8")
    for info in json.loads(file):
        return info


def sign_in(message):
    message_to_employee(message)
    email = input("Write your email: ")
    password = input("Write your password: ")
    account = account_valid(email)
    if account:
        data = to_get_data(employee_path())
    else:
        print("Invalid email, please check out your email")
