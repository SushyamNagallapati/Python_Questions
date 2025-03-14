numbers = list(map(int, input("Enter number with spaces: ").split()))

count_dict = {}

max_count = 0
most_frequent_number = 0

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
        
for key, value in count_dict.items():
    if value > max_count:
        max_count = value
        most_frequent_number = key
        
for key, value in count_dict.items():
    print(f"{key}: {value} time{'s' if value > 1 else ''}")
    
print(f"The most frequent number is: {most_frequent_number} appears {max_count} times")
