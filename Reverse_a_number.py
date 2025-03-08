number = int(input("Enter a number: "))
reverse_number = 0

while number > 0:
    reverse_number = reverse_number * 10 + (number % 10)
    number //= 10    
print(reverse_number)
