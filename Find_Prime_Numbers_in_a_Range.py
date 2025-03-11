start, end = map(int, input("Enter a number: ").split())

prime_numbers = []

for num in range(start, end + 1):
    if num < 2:
        continue
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        prime_numbers.append(num)
        
print(f"The Prime Numbers between {start} and {end} are: {prime_numbers}")
