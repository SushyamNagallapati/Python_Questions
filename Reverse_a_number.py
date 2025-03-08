number = int(input("Enter a number: "))
reverse_number = 0

while number > 0:
    
    remainder = number % 10
    reverse_number = reverse_number * 10 + remainder
    number //= 10    
    
print(reverse_number)
