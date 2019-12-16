class Book:

    def __init__(self, title, author='', isbn='', price=0, count=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.count = count

    def sell(self):
        pass

    def restock(self, count):
        pass


class Bookstore:

    def __init__(self):
        self.books = []

    def restock_bookstore(self, book, count):
        pass

