n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))

n3 = input("Choose any one '+' '-' '*' '/': ")

if n3 == "+":
    print("The result is: ", n1 + n2)
elif n3 == "-":
    print("The result is: ", n1 - n2)
elif n3 == "*":
    print("The result is: ", n1 * n2)
elif n3 == "/":
    if n2 == 0:
        print("Invalid number")
    else:
        print("The result is: ", n1 / n2)
