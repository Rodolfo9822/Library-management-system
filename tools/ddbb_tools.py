import re
import json

# Global functions


def use_data_base(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def add_new_data(path, new_data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(json.dumps(new_data))


def account_valid(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    if (re.fullmatch(regex, email)):
        return True


def show_data(path):
    books = use_data_base(path)
    for book in books:
        better_presentation(book)


def better_presentation(book):
    print("")
    for tag, info in book.items():
        print(f"{tag.capitalize()}: {info}")


def does_it_exist(_id, path):
    data = use_data_base(path)
    return list(filter(lambda el: el["id"] == _id, data))


def delete_element(_id, path):
    is_there = does_it_exist(_id, path)
    if (is_there):
        old_info = use_data_base(path)
        new_DDBB = list(filter(lambda x: x["id"] != _id, old_info))
        add_new_data(path, new_DDBB)
        return (True, is_there)
    else:
        print(f"\nError, The id you've written doesn't exist")
        return (False, "")


def saving_data(data, path, message):
    whole_data = use_data_base(path)
    whole_data.append(data)
    add_new_data(path, whole_data)
    print(f"\n{message}")


# Path JSON


def employees_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/employee_data.json"


def members_path():
    return ""


def books_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/books_warehouse.json"


def borrowed_path():
    return "C:/Users/PC/Desktop/Python/Projects/Library_Management_System/DDBB/borrowed_books_warehouse.json"

# DDBB functions for employees


def sign_in(message):
    print(message)
    email = input("Write your email: ")
    password = input("Write your password: ")
    account = account_valid(email)
    if account:
        outcome = validate_account(email, password)
        if outcome is not None:
            return True, outcome
        else:
            return False, ""
    else:
        print("Invalid email, please check out your email")
        return False, ""


def validate_account(user_email, user_pass):
    file = use_data_base(employees_path())
    for employee in file:
        email = employee["email"]
        password = employee["password"]
        if email == user_email and password == user_pass:
            return employee

# DDBB functions for books


def book_selected(_id):
    books = use_data_base(books_path())
    return list(filter(lambda b: b["id"] == _id, books))
