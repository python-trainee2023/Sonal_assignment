
# take the input for the start and stop value for a range.
# Then get the sum of odd and even numbers within that range using function or lambda and display that.

start = int(input("enter start value"))
stop = int(input("enter stop value"))


num = list(range (start, stop+1))
print(num)

even = sum(list(filter(lambda x : x%2 == 0, num)))
odd = sum(list(filter(lambda x: x%2 != 0, num)))

print("even sum",even, ",odd sum ",odd)
