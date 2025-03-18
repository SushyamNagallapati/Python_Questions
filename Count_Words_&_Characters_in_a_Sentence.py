# sentence = input("Enter sentence: ").lower()

# characters = len(sentence)

# words = len(sentence.split())

# print(f"The number of characters in the given sentence is: {characters}")
# print(f"The number of words in the given sentence is: {words}")


# # OR


sentence = input("Enter sentence: ").lower()

characters_with_spaces = len(sentence)

characters_without_spaces = len(sentence.replace(" ", ""))

words = len(sentence.split())

print(f"The number of characters (with spaces) in the given sentence is: {characters_with_spaces}")
print(f"The number of characters (without spaces) in the given sentence is: {characters_without_spaces}")
print(f"The number of words in the given sentence is: {words}")
