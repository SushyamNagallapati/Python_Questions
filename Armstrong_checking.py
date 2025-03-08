number = int(input("Enter a number: "))

original_number = number

reverse_number = 0

while number > 0:
    remainder = number % 10
    reverse_number = reverse_number + remainder * remainder * remainder
    number //= 10
    
if original_number == reverse_number:
    print("This is an armstrong number")
else:
    print("This is not a Armstrong number")
