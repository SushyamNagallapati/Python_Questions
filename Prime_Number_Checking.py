number = int(input("Enter a number: "))      

if number < 2:
    print("Its not a prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Its not a prime number")
            break
    else:
        print("Its a prime number")
