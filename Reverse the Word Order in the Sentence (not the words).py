sentence = input("Enter a sentence: ").split()

reverse_words = sentence[::-1] # Reverses the word order not the words
    
result = " ".join(reverse_words) # Joining the reversed word order into a sentence

print(f"Reversed the word order: {result}")
