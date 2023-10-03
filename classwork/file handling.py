# file handling

# file = open("test.txt", "r").read()

# file = open("test.txt", "r").read(9)
# print(file)

# file = open("test.txt", "r")
# print(file.read(9))

# this returns in list form
# print(file.readlines())

# for x in file:
#     print(x)

# w -> write on existing file, overwrite old content and write new
# a append on existing content
# w+, a+ -> includes read too

# file = open("test.txt", "a")
# file.write("\nappendinggggggggggg")
# file.close()

# --------try except finally--------------------

try:
    with open("stud.txt", "r") as f:
        student = f.readlines()
        print(student)
except FileNotFoundError:
    print("file not found")
finally:
    print("in finalllyyy")

# ---------raise------------------
x=0
if x == 0:
    raise ValueError("value cant be zero")