import random

number = random.randint(1, 100)
attempts = 0
max_attempts = 5

while True:
    guess = int(input("Enter a number: "))
    attempts += 1
    
    if guess == number:
        print(f"Guessed Correctly in {attempts} attempt(s)!")
        break

    elif guess < number:
        print("Too Low")
    else:
        print("Too High")
        
    if attempts == max_attempts:
        print(f"Game Over, the correct number is '{number}'")
        break
