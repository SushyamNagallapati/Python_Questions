number = int(input("Enter a number: "))

perfect_number = 0

for i in range(1, number):
    if number % i == 0:
        perfect_number += i

if perfect_number == number:
    print("It is a Perfect Number")
else:
    print("Not a Perfect Number")
