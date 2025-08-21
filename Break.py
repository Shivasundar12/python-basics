# 1. break → Stop the loop completely
#Ends the loop right away, even if there are more items left to process.

#Used when you found what you were looking for and don’t need to continue.

# exmaple of break statement

age = 20
for i in range(5):
    if i == age:
        print("Found the age:", i)
        break  # Stop the loop when age is found
    print("Current number:", i)


for n in range(1, 10):
    if n == 5:
        break   # stop the loop entirely when n == 5
    print(n)

# What it does: Ends the current loop immediately and moves execution to the code after that loop.

# Where it works: only inside loops (for, while).


# return using break in a while loop


import random

secret_number = random.randint(1, 100)
max_attempts = 10
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
print(f"You have {max_attempts} attempts to guess it!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1   # increase attempts every guess

    if guess == secret_number:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
        break   # exit loop when correct guess
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

    if attempts >= max_attempts:
        print(f"❌ Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")
        break   # exit when attempts are over

