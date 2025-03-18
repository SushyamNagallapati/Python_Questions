sentence = input("Enter a sentence: ").lower()

count = {}

for i in sentence:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1
        
for key, value in count.items():
    if value == 1 and  key != " ":
        print(f"{key}")
