# 2. take input n and then display the factorial of that number

def factorial(num):
    fact = 1
    for x in range (num,0, -1):
        print("num :", x)
        fact = fact * x
    print(fact)


factorial(int(input("input number to find factorial")))
