import logging
import sys


#Create a logger
library_log = logging.getLogger(__name__)
library_log.setLevel(logging.INFO)

#Creating the Handler (Writing to a file)
file_handler = logging.FileHandler("library.log")


#Creating a Formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


#Add a formatter to handler
file_handler.setFormatter(formatter)


#Add handler to logger
library_log.addHandler(file_handler)

print("The books are: ")
books = {
    "A": "Harry Potter",
    "B": "The Hobbit",
    "C": "Sherlock Holmes",
    "D": "1984",
    "E": "End Checkout"
}


def show_book_menu():
    for book in books:
        print(f"[{book}] {books[book]}")
        
    titles = ", ".join(books.values())
    library_log.info(f"Menu contains: {titles}")


show_book_menu()

