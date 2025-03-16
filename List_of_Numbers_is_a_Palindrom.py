numbers = list(map(int, input("enter a number: ").split()))

if numbers == numbers[::-1]:
    print("It is a Palindrom number")
else:
    print("Not a Palindrom number")
