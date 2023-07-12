# Code to get student information 
from isbntools.app import *
print("\n")
print("~~ WELCOME TO THE ONLINE LIBRARY MANAGEMENT SYSTEM ~~~\n")
print("---------------------------------------------------------------\n")
name_of_student = input("Enter Your Full Name: ")
department_of_student = input("Enter Your Department: ")
year_of_student = input("Enter Your Academic Year: ")
roll_no_of_student = input("Enter Your Roll Number: ")
i= 0
while i<100:
     print("---------------------------------------------------------------\n")
     print("Welcome\t" +name_of_student + "\n")
     print('''Please enter a choice\n
     1. Search For A Book\n
     2. Get The Price Of A Book\n
     3. Issue A Book\n
     4. Exit\n''')
     options = int(input("Enter your choice: "))
     print("---------------------------------------------------------------\n")
     if(options==1):
         
         name_of_book = input("Enter The Name Of The Book: ")
         print("Book that you are searching for is: ", name_of_book)
         get_isbn = isbn_from_words(name_of_book)
         print(get_isbn)
         print(registry.bibformatters['labels'](meta(get_isbn)))
     elif(options==2):
         name_of_book = input("Enter The Name Of The Book: ")
         print("Book that you are searching for is: ", name_of_book)
         get_isbn = isbn_from_words(name_of_book)
         import random
         print("Price of the book is: ",random.randint(450,750))
     elif(options==3):
         name_of_book = input("Enter The Name Of The Book: ")
         get_isbn = isbn_from_words(name_of_book)
         print("ISBN number of book: " + get_isbn)
         print("\n")
         issue = int(input("For how many weeks do you want to issue the book? : "))
         print("\n")
         if(issue>=3):
             print("Sorry! we do not allow any student to issue a book more than 2 weeks")
             print("If you want to issue the book for more than 2 weeks, you can register for the same again")
         else:
             print("--------------------------------------------------\n")
             print(name_of_book)
             print("Issued By: " + name_of_student)
             print("Department: " + department_of_student)
             print("Academic Year: " + year_of_student)
             print("Roll No: " + roll_no_of_student)
             print("Thank You For Issuing The Book, You Can Collect The Book From The College Library By Showing Your ID\n")
             print("~~ THANK YOU FOR VISITING ONLINE LIBRARY MANAGEMENT SYSTEM ~~\n")
             break
     else:
          print("~~ THANK YOU FOR VISITING ONLINE LIBRARY MANAGEMENT SYSTEM ~~")
          break
     i = i+1 
else:
         print("~~ THANK YOU FOR VISITING ONLINE LIBRARY MANAGEMENT SYSTEM ~~")



