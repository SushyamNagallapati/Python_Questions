# # Sum of First N Natural Numbers

number = int(input("Enter a number: "))
sum_of_numbers = 0

for i in range(1, number + 1):
    sum_of_numbers = sum_of_numbers + i
    
print(sum_of_numbers)


# # Or

n = int(input("enter a number: "))
add = sum(range(1, n + 1))
print(add)


# # Or

n = sum(range(1, int(input("Enter a number: ")) + 1))
print(n)
