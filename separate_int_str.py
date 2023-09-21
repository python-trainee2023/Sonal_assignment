#  to separate a list according to their type

user_input = input("enter mulitple values, separate by commma")
lists = user_input.split(',')
print("Given values:",lists)
strings = [x for x in lists if not x.isdigit()]
integers = [x for x in lists if x.isdigit()]
print("Strings:",strings)
print("Integers:",integers)