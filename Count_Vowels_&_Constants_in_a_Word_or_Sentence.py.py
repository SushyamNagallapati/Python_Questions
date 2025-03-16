word = input("Enter a word or sentecne: ").lower()

vowels = 0
constants = 0

for char in word:
    if char in "aeiou":
        vowels += 1
    elif char.isalpha():
        constants += 1
        
print(f"The number of Vowels present in the word or sentence: {vowels}")
print(f"The number of Constants present in the word or sentence: {constants}")
