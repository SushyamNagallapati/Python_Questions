rows = int(input("Enter a number: "))

num = 1 # Start counting from 1

for i in range(1, rows + 1):
    for j in range(i): # Print i numbers in each row
        print(num, end=" ")
        num += 1
    print() # Move to next line after each row
