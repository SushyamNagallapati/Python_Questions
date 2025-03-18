sentence = input("Enter a sentence: ")

upper_case = 0
lower_case = 0

for i in sentence:
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1
        
print(f"Number of Upper case letters present in the sentence: {upper_case}")
print(f"Number of Lower case letters present in the sentence: {lower_case}")
