from src.Book import Book
from src.User import User
from typing import List, Tuple

class Library:
    def __init__(self)->None:
        self.__books : List[Book]= []
        self.__users :List[User]= []
        self.__checked_out_books :List[Tuple[str,int,str]] = []
        self.__checked_in_books :List[Tuple[str,int,str]]= []

    # Getters
    def get_books(self)->list:
        return self.__books

    def get_users(self)->list:
        return self.__users

    def get_checked_out_books(self)->list:
        return self.__checked_out_books

    def get_checked_in_books(self)->list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn:str, title:str, author:str)->None:
        for book in self.__books:
            if book.get_isbn() == isbn:
                return
        libro : Book = Book(isbn, title, author)
        self.__books.append(libro)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(book.__str__())

    # 2.1 Check out book
    def check_out_book(self, isbn:str, dni:int, due_date:str)-> str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                for user in self.__users:
                    if user.get_dni() == dni:
                        if book.is_available():
                            user.increment_checkouts()
                            self.__checked_out_books.append((isbn, dni, due_date))
                            book.set_available(False)
                            book.increment_checkout_num()
                            return f"User {dni} checked out book {isbn}"
                        else:
                            return f"Book {isbn} is not available"

        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn:str, dni:int, returned_date:str)->str:
        for book in self.__books:
            if book.get_isbn() == isbn:
                if not book.is_available():
                    book.set_available(True)
                    for user in self.__users:
                        if user.get_dni() == dni:
                            user.increment_checkins()

                    self.__checked_in_books.append((isbn, dni, returned_date))
                    for libro in self.__checked_out_books:
                        if libro[0] == isbn:
                            self.__checked_out_books.remove(libro)
                            break
                    return f"Book {isbn} checked in by user {dni}"

        return f"Book {isbn} is not available"

    # Utils
    def add_user(self, dni: str, name: str) -> None:
        for user in self.__users:
            if user.get_dni() == dni:
                return
        usuario: User = User(dni, name)
        self.__users.append(usuario)