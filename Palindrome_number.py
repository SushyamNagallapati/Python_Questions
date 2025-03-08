number = int(input("Enter a number: "))

original_number = number
reverse_number = 0

while number > 0:
    remainder = number % 10
    reverse_number = reverse_number * 10 + remainder
    number //= 10
    
if original_number == reverse_number:
    print("The number is a Palindrome")
else:
    print("The number is not a Palindrome")
