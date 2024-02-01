from messages import identify_yourself
from logic import main_employee
from logic import main_member


def start():
    main_employee() if identify_yourself() == 1 else main_member()
