numbers = list(map(int, input("Enter numbers with spaces: ").split()))

for i in range(len(numbers) - 1):
    for j in range(len(numbers) - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers [j]
            
print("Sorted numbers: ", numbers)
