from functions import account_valid
import json
from pathlib import Path


def employees_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/employee_data.json"


def members_path():
    return ""


def books_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/books_warehouse.json"


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


def to_get_books(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def show_all_books():
    books = to_get_books(books_path())
    for book in books:
        better_presentation(book)


def better_presentation(book):
    print("")
    for tag, info in book.items():
        print(f"{tag.capitalize()}: {info}")


def book_selected(_id):
    books = to_get_books(books_path())
    return list(filter(lambda b: b["id"] == _id, books))


def sign_in(message):
    print(message)
    email = input("Write your email: ")
    password = input("Write your password: ")
    account = account_valid(email)
    if account:
        data = to_get_data(employees_path(), email, password)
        return data
    else:
        print("Invalid email, please check out your email")
        return False, ""
