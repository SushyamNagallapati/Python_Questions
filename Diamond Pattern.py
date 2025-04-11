number = int(input("Enter a number: "))

for i in range(1, number + 1):
    print(" " * (number - i), end="")
    for j in range(i):
        print("* ", end="")
    
    print()
        
for k in range(number - 1, 0, -1):
    print(" " * (number - k), end="")
    for p in range(k):
        print("* ", end="")
        
    print()
