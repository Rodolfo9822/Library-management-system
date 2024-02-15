from abc import ABC
from tools import show_data, book_selected, better_presentation, books_path, borrowed_path, delete_element, employees_path
from functions import book_id_ok, book_fields, employee_fields
from messages import error_message


class Person(ABC):
    def __init__(self, _id, name, last_name, email, password, phone):
        self._id = _id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone

    def adding(self):
        print("")

    def removing(self):
        pass

    def searchFor(self):
        book_id = input(
            "Please, to write the book id would you want to look for? ")
        if (book_id_ok(book_id)):
            book = book_selected(book_id)[0]
            print(f"\nThe book you've selected is {book['title']}")
            better_presentation(book)
        else:
            print("\nYour choice don't exist, please, check out the ID")

    def get_id(self):
        return self._id

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def get_last_name(self):
        return self.last_name

    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone


class Employee(Person):
    def __init__(self, _id, name, last_name, email, password, phone, schedule, job):
        super().__init__(_id, name, last_name, email, password, phone)
        self.schedule = schedule
        self.job = job

    def adding(self):
        option = input("""To add a new book to the data base you have write Yes and you will be filling out the fields.
if you want to cancel the action, write No.
                        """)
        if option.capitalize() == "Yes":
            book_fields()
        elif option.capitalize() == "No":
            print("\nYou've cancel the action, you got back to the menu")
        else:
            error_message("You haven't selected one of the options")

    def whole_book_DDBB(self):
        show_data(books_path())

    def whole_borrowed_book(self):
        show_data(borrowed_path())

    def set_schedule(self, new_schedule):
        self.schedule = new_schedule

    def get_schedule(self):
        return self.schedule

    def set_job(self, new_job):
        self.job = new_job

    def get_job(self):
        return self.job

    def new_user(self):
        pass

    def user_deleted(self):
        pass

    def whole_employee_DDBB(self):
        show_data(employees_path())

    def new_employee(self):
        employee_fields()

    def edit_employee(self):
        decision = input(
            "Are you actually sure to change the book information?, Write yes to proceed with , or you can write No to cancel the action. ")
        if decision.capitalize() == "Yes":
            _id = input("Write the employee id ")
            outcome, information = delete_element(_id, employees_path())
            if outcome:
                better_presentation(information[0])
                employee_fields(_id, True)

    def fire_employee(self):
        decision = input(
            "Are you actually sure to fire an employee? write Yes to proceed with it, or write No to cancel the action ")
        if decision.capitalize() == "Yes":
            _id = input("Write the employee id ")
            outcome, info = delete_element(_id, employees_path())
            if outcome:
                print(f"You've fired {info[0]['name']} {info[0]['lastName']}")

    def details_borrowed_books(self):
        pass

    def book_deleted(self):
        choice = input(
            "Are you actually sure to delete a book?, to cancel the action you have to write No if you want to continue writing Yes. ")
        if choice.capitalize() == "Yes":
            book_id = input("To write the book id ")
            outcome, book = delete_element(book_id, books_path())
            if outcome:
                print(f"\nYou've removed the book {book[0]['title']}")

    def edit_book(self):
        _id = input(
            "If you want to changes the book information, please write its id ")
        state, deleted_book = delete_element(_id, books_path())
        if state:
            better_presentation(deleted_book[0])
            print("\n You actually can use the information about to rewrite once again, be careful to changes data")
            book_fields(_id, True)

    def get_user_data(self):
        pass

    def edit_user(self):
        pass


class Member(Person):

    def __init__(self, _id, name, last_name, email, password, phone, registration_date, address, blocked, debt, date_borrowed):
        super().__init__(_id, name, last_name, email, password, phone)
        self.registration_date = registration_date
        self.address = address
        self.blocked = blocked
        self.debt = debt
        self.date_borrowed = date_borrowed

    def get_registration_date(self):
        return self.registration_date

    def set_address(self, new_addres):
        self.address = new_addres

    def get_address(self):
        return self.address

    def set_date_borrowed(self, update_date_borrowed):
        self.date_borrowed = update_date_borrowed

    def get_date_borrowed(self):
        return self.date_borrowed

    def set_debt(self, update_debt):
        self.debt = update_debt

    def get_debt(self):
        return self.debt

    def set_blocked(self, update_blocked):
        self.blocked = update_blocked

    def get_blocked(self):
        return self.blocked

    def details_borrowed_books(self):
        pass

    def their_data(self):
        return (self._id, self.name, self.last_name, self.email, self.password, self.phone, self.registration_date, self.address, self.blocked, self.debt, self.date_borrowed)
