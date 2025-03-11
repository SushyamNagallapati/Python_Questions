number = list(map(int, input("Enter numbers: ").split()))

count_dict = {}

for num in number:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1
        
for key, value in count_dict.items():
    print(f"{key}: {value} time{'s' if value > 1 else ''}")
