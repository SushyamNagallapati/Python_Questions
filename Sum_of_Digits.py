# # Sum of Digits
number = int(input("Enter a number: "))

sum = 0

while number > 0:
    
    remainder = number % 10
    sum += remainder
    number //= 10
    
print(sum)
