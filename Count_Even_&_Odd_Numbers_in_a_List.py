numbers = list(map(int, input("Enter numbers with spaces: ").split()))

even_numbers = 0
odd_numbers = 0

for num in numbers:
    if num % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
        
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
