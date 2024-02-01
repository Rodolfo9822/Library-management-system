from tools import Mistake


def identify_yourself():
    try:
        user = int(input("""Welcome to the Book Haven, before looking for book in our whole warehouse
can you identify yourself, just write the number of the option which is below. 
        1.- Employee
        2.- Member
          """))
        if user in (1, 2):
            return user
        else:
            raise Mistake("You had to choose the number 1 or number 2")
    except ValueError:
        print("Error, you have writen letters")


def message_to_employee(message):
    print(message)
