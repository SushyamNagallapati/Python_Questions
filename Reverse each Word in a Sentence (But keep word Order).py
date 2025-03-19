sentence = input("Enter a sentence: ").split()

reverse_words = []

for i in sentence:
    reverse_words.append(i[::-1])
    
result = " ".join(reverse_words)

print(f"Reversed sentence: {result}")
