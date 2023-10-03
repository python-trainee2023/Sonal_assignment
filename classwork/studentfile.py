# Create a file ‘student.txt’ that contains students’ name,
# gender, and grade. Write a program to read individual lines
# and copy each line of the file and write in another file using for loop.
# The content should be in uppercase. Use context manager.


# file = open("student.txt", "r")
# fileList = file.readlines()
#
# for x in fileList:
#     file = open("student1.txt","w")
#     file.write(x)


# class FileManager:
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode
#
#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()
#
#
# with FileManager("student.txt", "r") as f, FileManager("student2.txt", "w") as s:
#     student = f.readlines()
#     for x in student:
#         s.write(x.upper())

# can be made with class or by using open

with open("../student.txt", "r") as f, open("../student2.txt", "w") as s:
    student = f.readlines()
    for x in student:
        s.write(x.upper())

print(s.closed)


