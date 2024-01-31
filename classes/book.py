class Book:
    def __init__(self, _id, title, author, pages, kind_of, genre, quantity, available):
        self._id = _id
        self.title = title
        self.author = author
        self.pages = pages
        self.kind_of = kind_of
        self.genre = genre
        self.quantity = quantity
        self.available = available

    def get_id(self):
        return self._id

    def set_title(self, update_title):
        self.title = update_title

    def get_title(self):
        return self.title

    def set_author(self, update_author):
        self.author = update_author

    def get_author(self):
        return self.author

    def set_pages(self, update_pages):
        self.pages = update_pages

    def get_pages(self):
        return self.pages

    def set_kind_of(self, update_kind_of):
        self.kind_of = update_kind_of

    def get_kind_of(self):
        return self.kind_of

    def set_genre(self, update_genre):
        self.title = update_genre

    def get_genre(self):
        return self.genre

    def set_quantity(self, update_quantity):
        self.title = update_quantity

    def get_quantity(self):
        return self.quantity

    def set_available(self, update_available):
        self.title = update_available

    def get_available(self):
        return self.available

    def bring_data(self):
        return (self._id, self.title, self.author, self.pages, self.kind_of, self.genre, self.quantity, self.available)
