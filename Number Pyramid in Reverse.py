row = int(input("Enter a number: "))

num = 1

for i in range(1, row + 1):
    for s in range(row - i): 
        print(" ", end=" ") # Print spaces before numbers
    for j in range(i):
        print(num, end=" ")
        num +=1 
    print() # Move to the next line after each row
