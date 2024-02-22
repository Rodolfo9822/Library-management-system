from tools import sign_in
from messages import employee_menu, error_message
from classes import Employee
from tools import Mistake, employees_path


def execute_action(choice, user):
    match choice:
        case 1: user.searchFor()
        case 2: user.whole_book_DDBB()
        case 3: user.whole_borrowed_book()
        case 4: user.adding()
        case 5: user.edit_book()
        case 6: user.book_deleted()
        case 7: user.whole_employee_DDBB()
        case 8: user.new_employee()
        case 9: user.edit_employee()
        case 10: user.fire_employee()
        case 11: user.whole_member_DDBB()
        case 12: user.new_member()
        case 13: user.edit_user()
        case 14: user.look_member()
        case 15: user.delete_member()
        case _: pass


def bunch_of_choices(choice, user):
    execute_action(choice, user)


def building(data):
    return Employee(data["id"], data["name"], data["lastName"], data["email"], data["password"], data["phone"], data["schedule"], data["job"])


def main_employee():
    print("")
    state, data = sign_in(
        "Book Haven system, please typing your email and password to get access to the sytem", employees_path())
    if state:
        user = building(data)
    while (state):
        print("")
        try:
            number_options = 16
            choice = employee_menu(user.get_name(), user.get_last_name())
            if choice >= 1 and choice <= number_options:
                if choice == number_options:
                    state = False
                else:
                    bunch_of_choices(choice, user)
            else:
                raise Mistake("You haven't selected one of the options")
        except ValueError:
            error_message("You have written words")
