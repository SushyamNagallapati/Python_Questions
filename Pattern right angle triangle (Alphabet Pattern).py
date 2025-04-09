number_of_lines = int(input("Enter a number: "))

for i in range(1, number_of_lines + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
        
    print()
