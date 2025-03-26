row = int(input("Enter a number: "))

num = 1

for i in range(1, row + 1):
    for s in range(row - i): 
        print(" ", end=" ")
    for j in range(i):
        print(num, end=" ")
        num +=1 
    print()
