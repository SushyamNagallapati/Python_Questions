numbers = list(map(int, input("Enter numbers with spaces: ").split()))

positive_numbers = []
negative_numbers = []

for i in numbers:
    if i >= 0:
        positive_numbers.append(i)
    else:
        negative_numbers.append(i)
        
print(f"Positive Numbers: {positive_numbers}")
print(f"Negative Numbers: {negative_numbers}")
