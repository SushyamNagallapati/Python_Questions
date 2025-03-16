# numbers = list(map(int, input("Enter number with spaces: ").split()))

# smallest_numbers = min(numbers)
# largest_numbers = max(numbers)

# print(f"The smallest number in the list is: {smallest_numbers}")
# print(f"The largest number in the list is: {largest_numbers}")


# # OR


numbers = list(map(int, input("Enter number with spaces: ").split()))

smallest_numbers = numbers[0]
largest_numbers = numbers[0]

for num in numbers: 
    if num < smallest_numbers:
        smallest_numbers = num
    elif num > largest_numbers:
        largest_numbers = num
        
print(f"The smallest number in the list is: {smallest_numbers}")
print(f"The largest number in the list is: {largest_numbers}")
