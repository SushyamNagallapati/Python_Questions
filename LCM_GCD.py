a = int(input("Enter a number: "))

b = int(input("Enter a number: "))

t1, t2 = a, b

while b != 0:
    remainder = a % b
    a, b = b, remainder
    
GCD = a
LCM = (t1 * t2) / GCD

print(f"The GCD for the given numbers is {GCD}")
print(f"The LCM for the given numbers is {LCM}")
