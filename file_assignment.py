# Assignment

# 1.Write a Python program that manages book records using a file called book.txt.
# The program should ask the user to input an author's name.
# It should then search through the records in the book.txt file and
# display all the records for books written by the given author.
# The programs should handle the exceptions as well.

find_author = input("enter the name of author to find their book")
author_found = False
try:
    with open("book.txt", "r") as file:
        for x in file:
            author, book = x.strip().split(", ")
            if author == find_author:
                print(f"book: {book}\nauthor: {author}")
                author_found = True
    if not author_found:
        print(f"author {find_author} not found in book.txt")

# except FileNotFoundError:
#     print("file doesnt exist")

except Exception as e:
    print(f"an error occured::{str(e)}")
