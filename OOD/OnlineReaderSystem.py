class Book:
    """
    Book
    """
    def __init__(self, book_id, details):
        self.__book_id = book_id
        self.details = details

    def update(self):
        pass

    def get_book_id(self):
        return self.__book_id

    def set_book_id(self, book_id):
        self.__book_id = book_id

    def get_book_details(self):
        return self.details

    def set_book_details(self, details):
        self.details = details


class User:
    """
    User
    """
    def __init__(self, user_id, details, account_type):
        self.__user_id = user_id
        self.details = details
        self.account_type = account_type

    def renew_membership(self):
        pass

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def get_user_details(self):
        return self.details

    def set_user_details(self, details):
        self.details = details

    def get_account_type(self):
        return self.account_type

    def set_account_type(self, account_type):
        self.account_type = account_type


class UserManager:
    """
    User Manager
    """
    def __init__(self):
        self.users = {}

    def add_user(self, user_id, details, account_type):
        if user_id in self.users:
            return None
        else:
            user = User(user_id, details, account_type)
            self.users[user_id] = user
            return user

    def remove_user_by_id(self, user_id):
        if user_id not in self.users:
            return False
        else:
            del self.users[user_id]

    def remove_user(self, user):
        self.remove_user_by_id(user.get_user_id())

    def find_user(self, user_id):
        return self.users.get(user_id)


class Library:
    """
    Library which manages books
    """
    def __init__(self):
        self.books = {}

    def add_book(self, book_id, details):
        if book_id in self.books:
            return None
        else:
            book = Book(book_id, details)
            self.books[book_id] = book
            return book

    def remove_book_by_id(self, book_id):
        if book_id not in self.books:
            return False
        else:
            del self.books[book_id]

    def remove_book(self, book):
        self.remove_book_by_id(book.get_book_id())

    def find_book(self, book_id):
        return self.books.get(book_id)


class Display:
    """
    Display
    """
    def __init__(self):
        self.__active_book = None
        self.__active_user = None
        self.__page_number = 0

    def refresh_user_name(self):
        """
        Update user name display

        :return:
        """
        print("User: %s" % self.__active_user.get_user_details())

    def refresh_title(self):
        """
        Update title display

        :return:
        """
        print("Reading book: %s" % self.__active_book.get_book_details())

    def refresh_details(self):
        """
        Update details display

        :return:
        """
        print("Reading book: %d" % self.__active_book.get_book_details())

    def refresh_page(self):
        """
        Update page display

        :return:
        """
        print("Reading page %d" % self.__page_number)

    def turn_page_forward(self):
        self.__page_number += 1
        self.refresh_page()

    def turn_page_backward(self):
        self.__page_number -= 1
        self.refresh_page()

    def display_user(self, user):
        self.__active_user = user
        self.refresh_user_name()

    def display_book(self, book):
        self.__page_number = 0
        self.__active_book = book
        self.refresh_title()
        self.refresh_details()
        self.refresh_page()


class OnlineReaderSystem:
    """
    Online Reader System
    """
    def __init__(self):
        self.__user_manager = UserManager()
        self.__library = Library()
        self.__display = Display()
        self.__active_book = None
        self.__active_user = None

    def get_library(self):
        return self.__library

    def get_user_manager(self):
        return self.__user_manager

    def get_display(self):
        return self.__display

    def get_active_book(self):
        return self.__active_book

    def set_active_book(self, book):
        self.__active_book = book
        self.__display.display_book(book)

    def get_active_user(self):
        return self.__active_user

    def set_active_user(self, user):
        self.__active_user = user
        self.__display.display_user(user)
