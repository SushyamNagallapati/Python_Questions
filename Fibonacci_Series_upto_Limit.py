number = int(input("Enter a number: "))

if number < 0:
    print("You have entered Invalid number")
else:
    a = 0
    b = 1
    print(a)
    
    if number > 0:
        print(b)
        
    while True:
        c = a + b
        if c >= number:
            break
        print(c)
        a = b
        b = c
