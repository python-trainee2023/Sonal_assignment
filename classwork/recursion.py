# recursion
# lambda function


# add = lambda a,b:a+b
# print(add(3,4))

# num=[1,2,3,4,5,6]
# even = list(filter(lambda x: x%2 == 0, num))
# print(even)

# map function takes each element from given list
# square = list(map(lambda x: x**2, num))
# print(square)

# operation = [lambda x, y:x+y, lambda x, y:x-y]
# val1 = operation[0](3,4)
# val2 = operation[1](9,6)
# print(val1, val2)

# shadowing
# inner scope ko var le outer ko lai shadow garxa
# should be prevented

# x= 1
# def test():
#     x=3
#     print(x)
#
# print(x)

# can be done like this

# x= 1
# def test():
#     global x
#     x=3
#     print(x)

# nonlocal, function level ko shadowning hataune




