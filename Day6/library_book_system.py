menu = """
    ------------------
    WELCOME TO LIBRARY
    ------------------
    1. View Available Books
    2. Borrow a Book
    3. Return a Book
    4. Exit
"""

available_books = ["Harry Potter", "Crime and Punishment", "DSA and Algorithms", "Book4"]

print(menu)
option = input("Enter the option: ")


while option != "4":
    if option == "1":
        print(f"The list of available books are: {available_books}")

    elif option == "2":
        number_of_books = len(available_books)
        for number in range(number_of_books):
            print(f"{number}. {available_books[number]}")
        
        borrow_option = int(input("Enter the book number: "))

        if borrow_option + 1 > number_of_books:
            print("Option Unavailable")
            break

        borrowed_book = available_books[borrow_option]
        available_books.remove(borrowed_book)
        print(f"You borrowed {borrowed_book} successfully")

    elif option == "3":
        book_to_return = input("Enter the book you want to return: ")
        available_books.append(book_to_return)
        print(available_books)
    
    print(menu)
    option = input("Enter the option: ")
