number = int(input("Enter a number: "))

num = 1

for i in range(1, number + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
        
    print()
