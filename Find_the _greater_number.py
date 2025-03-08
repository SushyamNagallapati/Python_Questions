# # Find the largest number

a = int(input("Enter a number: "))

b = int(input("Enter a number: "))

c = int(input("Enter a number: "))

if a >= b and a >= c:
    print("A is greater")
elif b >= a and  b >= c:
    print("B is greater")
else:
    print("C is greater")
