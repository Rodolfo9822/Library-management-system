from messages import identify_yourself
from logic import main_employee
from logic import main_member


def start():
    state = True
    while (state):
        option = identify_yourself()
        match option:
            case 1:
                main_employee()
            case 2:
                main_member()
            case 3:
                state = False
            case _:
                pass
