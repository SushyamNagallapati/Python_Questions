number = list(map(int, input("Enter number with spaces: ").split()))

number_of_times = {}

for i in number:
    if i in number_of_times:
        number_of_times[i] += 1
    else:
        number_of_times[i] = 1
        
for key, value in number_of_times.items():
    print(f"{key} is printed {value} time{'s' if value > 1 else ''}")
