from tools import sign_in


def main_employee():
    information = sign_in(
        "Welcome to the system of the library, please typing your email and password to get access to the sytem")
    print(information)
