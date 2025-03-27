a = list(map(int, input("Enter number with spaces: ").split()))
b = list(map(int, input("Enter number with spaces: ").split()))

c = []

max_len = max(len(a), len(b))

for i in range(max_len):
    if i < len(a):
        c.append(a[i])
    if i < len(b):
        c.append(b[i])
        
print(f"Merged List: {c}")
