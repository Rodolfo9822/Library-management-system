import time
from messages import error_message
from tools import saving_data, books_path, employees_path, account_valid, members_path
from datetime import datetime


def currently_date(whole):
    return str(datetime.now())[:whole]


def book_id_ok(_id):
    if (len(_id) == 11):
        return True


def generate_id(stuff):
    _id = ""
    if len(stuff) < 7:
        stuff = stuff.replace(" ", "")[0:4]
        _id = f"{stuff}{str(time.time())[-8:-1]}"
    else:
        stuff = stuff.replace(" ", "")[0:7]
        _id = f"{stuff}{str(time.time())[-5:-1]}"
    return _id


def to_block_member(money):
    return "Blocked" if money > 0 else "No blocked"


def save_data(field_data, identifier, path, message):
    data_dict = {}
    for index in range(0, len(identifier)):
        data_dict.setdefault(identifier[index], field_data[index])
    saving_data(
        data_dict, path, message)

# function to books


def is_there_mistakes(field_data):
    return "false" in field_data


def two_options(message, choices=[]):
    stuff = input(message).capitalize()
    return stuff if stuff in choices else "false"


def book_fields(likely_id="", editing=False):
    field_list = []
    try:
        title = input("What is the title of the book? ")
        if editing:
            field_list.append(likely_id)
        else:
            field_list.append(generate_id(title))
        field_list.append(title)
        field_list.append(input(f"Who is the author of {title}? "))
        field_list.append(int(input(f"how many pages does {title} have? ")))
        field_list.append(two_options
                          (f"is {title} hardcover or paperback? ", ["Hardcover", "Paperback"]))
        field_list.append(input(f"What gender is {title}? "))
        quantity = int(input(f"How many books are available? "))
        field_list.append(quantity)
        field_list.append("It's available" if quantity >
                          0 else "It isn't available")
        field_list.append(two_options(
            f"is {title} an audibook?, only write Yes or No ", ["Yes", "No"]))
        if not is_there_mistakes(field_list):
            identifier = ["id", "title", "author", "pages", "type",
                          "genre", "quantity", "available", "audiobook",]
            message = "The book just has been stored correctly. You already can look for it now."
            save_data(field_list, identifier, books_path(), message)
        else:
            error_message("there are incorrect data in the fields")
    except ValueError:
        error_message("One of the field got incorrect data")


# Employee

def employee_fields(likely_id="", editing=False):
    field_list = []
    try:
        name = input("What is the name of the employee? ")
        if editing:
            field_list.append(likely_id)
        else:
            field_list.append(generate_id(name))
        field_list.append(name)
        field_list.append(input(f"what's the last name of {name}? "))
        email = input(f"What's the {name} email? ")
        field_list.append(email if account_valid(email) else "false")
        field_list.append(input("What's your password? "))
        field_list.append(input(f"What's {name} phone number? "))
        field_list.append(input(f"What's {name} schedule? "))
        field_list.append(input(f"What's {name} job? "))
        if not is_there_mistakes(field_list):
            identifier = ["id", "name", "lastName", "email",
                          "password", "phone", "schedule", "job"]
            message = "The employee data has been stored correctly"
            save_data(field_list, identifier, employees_path(), message)
        else:
            error_message("there are incorrect data in the fields")
    except ValueError:
        error_message("One of the field got incorrect data")

# member


def member_fields(likely_id="", editing=False):
    field_list = []
    try:
        name = input("What is the name of the employee? ")
        if editing:
            field_list.append(likely_id)
        else:
            field_list.append(generate_id(name))
        field_list.append(name)
        field_list.append(input(f"what's the last name of {name}? "))
        email = input(f"What's the {name} email? ")
        field_list.append(email if account_valid(email) else "false")
        field_list.append(input("What's your password? "))
        field_list.append(input(f"What's {name} phone number? "))
        field_list.append(currently_date(11))
        field_list.append(input(f"What's {name} address? "))
        debt = int(
            input("Does the user have to pay a debt? if it's No just write the number 0 "))
        field_list.append(to_block_member(debt))
        field_list.append(debt)
        field_list.append("")
        if not is_there_mistakes(field_list):
            identifier = ["id", "name", "lastName", "email", "password", "phone",
                          "registration", "address", "blocked", "debt", "date_borrowed"]
            message = "The member data has been stored correctly"
            save_data(field_list, identifier, members_path(), message)
        else:
            error_message("there are incorrect data in the fields")

    except ValueError:
        error_message("One of the field got incorrect data")
