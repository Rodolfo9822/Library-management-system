from tools import sign_in
from messages import employee_menu, error_message
from classes import Employee
from tools import Mistake


def execute_action(choice, user):
    match choice:
        case 1: user.searchFor()
        case 2: user.whole_book_DDBB()
        case 3: print("")
        case 4: print("")
        case 5: user.adding()
        case 6: print("")
        case 7: print("")
        case 8: print("")
        case 9: print("")
        case 10: print("")
        case 11: print("")
        case 12: print("")
        case 13: print("")
        case 14: print("")
        case _: pass


def bunch_of_choices(choice, user):
    execute_action(choice, user)


def building(data):
    return Employee(data["id"], data["name"], data["lastName"], data["email"], data["password"], data["phone"], data["schedule"], data["job"])


def main_employee():
    state, data = sign_in(
        "Welcome to the system of the library, please typing your email and password to get access to the sytem")
    if state:
        user = building(data)
    while (state):
        print("")
        try:
            choice = employee_menu(user.get_name(), user.get_last_name())
            if choice >= 1 and choice <= 15:
                if choice == 15:
                    state = False
                else:
                    bunch_of_choices(choice, user)
            else:
                raise Mistake("You haven't selected one of the options")
        except ValueError:
            error_message("You have written words")
