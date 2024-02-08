import time
from tools import saving_book


def book_id_ok(_id):
    if (len(_id) == 11):
        return True


def generate_id(stuff):
    stuff = stuff.replace(" ", "")[0:7]
    return f"{stuff}{str(time.time())[-4:-1]}"


# function to books

def book_dictionary(field_data):
    identifier = ["id", "title", "author", "pages",
                  "type", "genre", "quantity", "available", "audiobook",]
    book_dict = {}
    for index in range(0, len(identifier)-1):
        book_dict.setdefault(identifier[index], field_data[index])
    saving_book(book_dict)


def two_options(message, choices=[]):
    stuff = input(message).capitalize()
    return stuff if stuff in choices else "false"


def book_fields():
    title = input("Writing the title of the book ")
    author = input(f"Who is the author of {title}? ")
    pages = int(input(f"how many pages does {title} have? "))
    _type = two_options(
        f"is {title} hardcover or paperback? ", ["Hardcover", "Paperback"])
    genre = input(f"What gender is {title}? ")
    quantity = int(input(f"How many books are available? "))
    available = "It's available" if quantity > 0 else "It isn't available"
    audiobook = two_options(
        f"is {title} an audibook?, only write Yes or No ", ["Yes", "No"])
    _id = generate_id(title)
    book_dictionary([_id, title, author, pages, _type,
                    genre, quantity, available, audiobook])


""" def book_fields():
    try:
        title = input("Writing the title of the book ")
        author = input(f"Who is the author of {title}? ")
        pages = int(input(f"how many pages does {title} have? "))
        _type = two_options(
            f"is {title} hardcover or paperback? ", ["Hardcover", "Paperback"])
        genre = input(f"What gender is {title}? ")
        quantity = int(input(f"How many books are available? "))
        available = "It's available" if quantity > 0 else "It isn't available"
        audiobook = two_options(
            f"is {title} an audibook?, only write Yes or No ", ["Yes", "No"])
        _id = generate_id(title)
        print([_id, title, author, pages, _type,
               genre, quantity, available, audiobook])
        book_dictionary([_id, title, author, pages, _type,
                        genre, quantity, available, audiobook])
    except ValueError:
        error_message("One of the field got incorrect data") """
