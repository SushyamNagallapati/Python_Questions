sentence = input("Enter a sentence: ").lower().split()

count = 0

for i in sentence: # Loops through each word
    if i[0] in "aeiou": # Checks the first letter of each word
        count += 1 # If its a vowel adds 1 to the count
        
print(f"The number of words start with vowels i the given sentence are: {count}")
