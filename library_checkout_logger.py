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

#choosing the book 
book_choice = input("Please choose one of the above: ").upper()
if book_choice in books:
    library_log.info(f"The choosen book is:{books[book_choice]}")
elif book_choice.title() in books.values():
    for code, title in books.items():
        if title.upper() == book_choice:
            library_log.info(f"The choosen book is :{title}")
            break
else:
    library_log.error(f"The choosen book {book_choice} doesnt exist in the library")

book_quantity = int(input(f"Please enter the quanitity of {book_choice} books you would like: "))
if book_quantity > 5:
    library_log.warning("Only 5 copies are allowed")
elif book_quantity > 0 and book_quantity < 6:
    library_log.info(f"The User has taken {book_quantity} copies of {book_choice}")
    library_log.info("The Checkout Session has ended. ")
