numbers = list(map(int, input("Enter numbers with spaces: ").split()))

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
            
sorted_numbers = numbers
print("sorted numbers: ", numbers)

unique_numbers = list(set(sorted_numbers))

unique_numbers.sort()

if len(unique_numbers) > 1:
    print("The Second Largest Number is: ", unique_numbers [-2])
else:
    print("No Second Largest Number")
