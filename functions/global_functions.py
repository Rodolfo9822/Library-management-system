import time
from messages import error_message
from tools import saving_data, books_path


def book_id_ok(_id):
    if (len(_id) == 11):
        return True


def generate_id(stuff):
    stuff = stuff.replace(" ", "")[0:7]
    return f"{stuff}{str(time.time())[-4:-1]}"


# function to books

def is_there_mistakes(field_data):
    return "false" in field_data


def book_dictionary(field_data):
    identifier = ["id", "title", "author", "pages",
                  "type", "genre", "quantity", "available", "audiobook",]
    book_dict = {}
    for index in range(0, len(identifier)):
        book_dict.setdefault(identifier[index], field_data[index])
    saving_data(
        book_dict, books_path(), "The book just has been stored correctly. You already can look for it now.")


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
            book_dictionary(field_list)
        else:
            error_message("there are incorrect data in the fields")
    except ValueError:
        error_message("One of the field got incorrect data")
