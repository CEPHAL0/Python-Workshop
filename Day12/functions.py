menu = """
    ------------------
    WELCOME TO LIBRARY
    ------------------
    1. View Available Books
    2. Borrow a Book
    3. Return a Book
    4. Exit
"""


available_books = [
    "Harry Potter",
    "Crime and Punishment",
    "DSA and Algorithms",
]


def take_option():
    input_value = input("Enter the option: ")
    return input_value


def print_menu():
    print(menu)


def option1():
    # Prints the available books
    for book in available_books:
        print(book)


def option2(book_name):
    # Remove a book from the list
    available_books.remove(book_name)
    print(f"The {book_name} has been borrowed successfully")


def option3(book_name):
    # Return a book to the list
    available_books.append(book_name)
    print(f"The {book_name} has been returned successfully")


def main(option):
    if option == "1":
        option1()
    elif option == "2":
        book_name = input("Enter the book you want to borrow: ")
        option2(book_name=book_name)
    elif option == "3":
        book_name = input("Enter the book you want to return: ")
        option3(book_name=book_name)
    else:
        print("Thank you for visiting !!")