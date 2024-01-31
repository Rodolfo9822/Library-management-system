from abc import ABC


class Person(ABC):
    def __init__(self, _id, name, last_name, email, password, phone):
        self._id = _id
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone

    def adding(self):
        pass

    def removing(self):
        pass

    def searchFor(self):
        pass

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
        pass

    def removing(self):
        pass

    def search_for(self):
        pass

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

    def delete_user(self):
        pass

    def new_employee(self):
        pass

    def fire_employee(self):
        pass

    def details_borrowed_books(self):
        pass

    def edit_book(self):
        pass

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

    def adding(self):
        pass

    def removing(self):
        pass

    def search_for(self):
        pass

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