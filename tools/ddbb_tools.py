import re
import json
from pathlib import Path

# Global functions


def use_data_base(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def add_new_data(path, new_data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(new_data))


def account_valid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if (re.fullmatch(regex, email)):
        return True

# Path JSON


def employees_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/employee_data.json"


def members_path():
    return ""


def books_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/books_warehouse.json"

# DDBB functions for employees


def validate_account(user_email, user_pass):
    file = use_data_base(employees_path())
    for employee in file:
        exist = account_exist(employee, user_email, user_pass)
    return exist


def account_exist(employee, user_email, user_pass):
    email = employee["email"]
    password = employee["password"]
    if email == user_email and password == user_pass:
        return True, employee


def sign_in(message):
    print(message)
    email = input("Write your email: ")
    password = input("Write your password: ")
    account = account_valid(email)
    if account:
        data = validate_account(email, password)
        return data
    else:
        print("Invalid email, please check out your email")
        return False, ""


# DDBB functions for books
def show_all_books():
    books = use_data_base(books_path())
    for book in books:
        better_presentation(book)


def better_presentation(book):
    print("")
    for tag, info in book.items():
        print(f"{tag.capitalize()}: {info}")


def book_selected(_id):
    books = use_data_base(books_path())
    return list(filter(lambda b: b["id"] == _id, books))


def saving_book(data):
    books = use_data_base(books_path())
    books.append(data)
    add_new_data(books_path(), books)
