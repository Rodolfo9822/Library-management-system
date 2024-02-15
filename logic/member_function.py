
from tools import Mistake, sign_in, members_path
from classes import Member
from messages import member_menu, error_message


def execute_action(choice, user):
    match choice:
        case 1: user.searchFor()
        case _: pass


def building(data):

    return Member(data["id"], data["name"], data["lastName"], data["email"], data["password"], data["phone"], data["registration"], data["address"], data["blocked"], data["debt"], data["dateBorrowed"])


def main_member():
    outcome, data = sign_in(
        "Book Haven system, please typing your email and password to get access to the sytem", members_path())
    if outcome:
        member = building(data)
    while outcome:
        print("")
        try:
            number_options = 5
            choice = member_menu(member.get_name(), member.get_last_name())
            if choice >= 1 and choice <= number_options:
                if choice == number_options:
                    outcome = False
                else:
                    execute_action(choice, member)
            else:
                raise Mistake("You haven't selected one of the options")
        except ValueError:
            error_message("You have written words")
