# def func(s):
#     #docstrings
#     """
#
#     :param s:
#     :return:
#     """
#     print("calling from the function",s)
#     add = 5 + s
#     return add
#
#
# output = func(40)
# print(output)

# LEGB , local, enclosed, global, built in scope

# a = 5
#
# def test():
#     a = 10
#
#     def inside_test():
#         print("from insdie_test", a)
#
#     inside_test()
#
#
# test()

# non local variable

# def test():
#     a = 10
#
#     def inside_test():
#         nonlocal a
#         print("from insdie_test", a+5)
#
#     inside_test()
#
# test()

# take user input and cube it, use function

def cube(num):
    return num ** 3


output = cube(int(input("enter a number")))
print(output)

# n = int(input("enter a number"))
# output = cube(n)
# print(output)


# print(cube(int(input("enter a number"))))
