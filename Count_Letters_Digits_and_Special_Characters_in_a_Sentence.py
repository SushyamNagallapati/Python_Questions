

user = input("Enter a sentence: ").lower()


letters = 0
digits = 0
special_characters = 0

for i in user:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
    else:
        special_characters += 1
        
print(f"The number of Letters present in the given sentence is: {letters}")
print(f"The number of Digits present in the given sentence is: {digits}")
print(f"The number of Special Characters present in the given sentence is: {special_characters}")
