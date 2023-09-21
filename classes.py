# x = input("enter a string to check if it's palindrome")
# print("you entered:",x)
#
# rev = x[::-1]
# print("Reversed:",rev)
#
# if x == rev:
#     print("Palindrome!")
# else:
#     print("Not a palindrome.")

# for i in range(0,29,2):
#     print(i)

# num_list =list(range(3,31,3))
# print(num_list)

# num = 0
# while num != 10:
#     print(num)
#     num += 1

# for i in range(5):
#     if i == 9:
#         print("hi")
#         break
# else:
#     print("from else")

# prime number
# num = int(input("enter a number"))
# if num <=1:
#     print("not prime")
# else:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print("not prime")
#             break
#     else:
#         print("prime")

# num = [2,4,5,9,18,20]
# new=[]
# count = 0
# for i in num:
#     if (i % 2) == 0:
#         # new.append(i)
#         new.insert(count, i)
#         count+=1
# print(new)

# num = list(range(1,10))
# print(num)
# square=[x ** 2 for x in num]
# print(square)

# fruits =["baNana","apPle", "manGo"]
# cap=[x.capitalize() for x in fruits]
# print(cap)

# num =[1,2.5,4,5.5,6,7.7,8]
# integers=[x for x in num if type(x)==int]
# print(integers)

# a=input("input a")
# b=input("input b")
# c=input("input c")
#
# max_num= max(a,b,c)
# print("maximum: ",max_num)

# take input like this

# user_input = input('Enter 3 numbers separate by comma')
# input_list = user_input.split(',')
# values = [float(x) for x in input_list]
# max_val=max(values)
# print(max_val)

#  to separate a list according to their type

user_input = input("enter mulitple values, separate by commma")
lists = user_input.split(',')
print("Given values:",lists)
strings = [x for x in lists if not x.isdigit()]
integers = [x for x in lists if x.isdigit()]
print("Strings:",strings)
print("Integers:",integers)





