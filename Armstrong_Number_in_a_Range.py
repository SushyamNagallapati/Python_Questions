start, end = map(int, input("Enter Two Numbers: ").split())

armstrong_numbers = []

for num in range(start, end + 1):
    original_number = num
    
    sum_of_powers = 0

    num_digits = len(str(num))
    
    while num > 0:
        digit = num % 10
        sum_of_powers += digit ** num_digits
        num //= 10

    if sum_of_powers == original_number:
        armstrong_numbers.append(original_number)
        
print(f"Armstrog numbers between {start} and {end} are {armstrong_numbers}")
