number = int(input("Enter a number: "))

def c(n, k):
    factorial(n)
    factorial(k)
    factorial(n - k)
    return factorial(n) // (factorial(k) * factorial(n - k))
    
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
        
    return result

for j in range(0, number):
    print(" " * (number - j), end="")
    for p in range(0, j + 1):
        print(c(j, p), end=" ")
        
    print()
