# number = int(input("Enter a number: "))

# original_number = number

# reverse_number = 0

# while number > 0:
#     remainder = number % 10
#     reverse_number = reverse_number + remainder * remainder * remainder
#     number //= 10
    
# if original_number == reverse_number:
#     print("This is an armstrong number")
# else:
#     print("This is not a Armstrong number")


# Or


number = int(input("Enter a number: "))
original_number = number

sum_of_powers = 0

num_digits = len(str(number))

while number > 0:
    digit = number % 10
    sum_of_powers += digit ** num_digits
    number //= 10
    
if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number")
else:
    print(f"{original_number} is not an Armstrong number")
