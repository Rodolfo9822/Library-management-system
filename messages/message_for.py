from tools import Mistake


def identify_yourself():
    print("")
    try:
        user = int(input("""Welcome to the Book Haven, before looking for book in our whole warehouse
can you identify yourself, just write the number of the option which is below. 
        1.- Employee
        2.- Member
        3.- To get out from the system.
          """))
        if user in (1, 2, 3):
            return user
        else:
            raise Mistake("You had to choose the number 1 or number 2")
    except ValueError:
        error_message("Error, you have written words")


def employee_menu(name, last_name):
    print(f"""Welcome {name} {last_name} to the Book Haven, you have the next the options to browse the Book Haven, you should write the number of the option.
          1.-  Looking for a book
          2.-  Looking at the book DDBB
          3.-  Looking at the borrowed DDBB
          4.-  Adding a new book to the DDBB
          5.-  Editing a book
          6.-  Removing a book
          7.-  To look at co-worker DDBB
          8.-  To make a new co-worker
          9.-  To editing a co-worker
          10.- To remove co-worker
          11.- Looking at member DDBB
          12.- Making a new member
          13.- Editing a member
          14.- Looking at a member
          15.- Removing a member
          16.- To get out.
          """)
    return int(input("What would you want to do? "))


def error_message(message):
    print(f"Error!!!, {message}")
