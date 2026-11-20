# Library Management System

book_name = "Python Programming"
author = "Guido van Rossum"
price = 450

print("LIBRARY MANAGEMENT SYSTEM")
print("-------------------------")
print("Book Name:", book_name)
print("Author:", author)
print("Price: Rs.", price)


# Book Issue Functionality

def issue_book():
    print("\nBOOK ISSUE DETAILS")
    student_name = input("Enter Student Name: ")
    print("Book Issued Successfully!")
    print("Student Name:", student_name)
    print("Issued Book:", book_name)


issue_book()
# Book Issue Functionality

def issue_book():
    student_name = input("Enter Student Name: ")
    book_name = input("Enter Book Name: ")

    print("\n----- Book Issue Details -----")
    print("Student Name:", student_name)
    print("Book Name:", book_name)
    print("Book issued successfully!")

issue_book()