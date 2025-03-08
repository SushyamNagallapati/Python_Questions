# # Prime number or not

number = int(input("Enter a number: "))

if number <= 1:
    print("It is not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")    
        