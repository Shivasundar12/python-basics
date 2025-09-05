# what is if else statement in python?
# An if-else statement in Python is a control flow statement that allows you to execute certain blocks of code based on whether a condition is true or false. It helps in making decisions in your code.

#exmaple of if else statement 

age=int(input("Enter your age: "))
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# In this example, the program checks if the entered age is 18 or older. If it is, it prints "You are an adult." Otherwise, it prints "You are a minor."


# Problem 1: The Age-Restricted Website
# Scenario: A website requires users to be at least 13 years old to create an account.
# The "if" logic: IF the user's age is 13 or more, THEN let them create an account.

age = int(input("enter your age:"))

if age >= 13:
    print("You can create an account.")
else:
    print("You are not old enough to create an account.")


# Problem 2: The Smart Thermostat
# Scenario: You want a program to turn on a fan only if the room gets too warm.
# The "if" logic: IF the temperature is above 78 degrees, THEN turn on the fan.
temp = int(input("Enter the room temperature: "))
if temp > 78:
    print( "Turning on the fan." )
else:
    print( "The room is comfortable." )


# Problem 3: The Secure Door
# Scenario: A door has a keypad and only opens if you enter the correct code.
# The "if" logic: IF the entered code matches the secret code, THEN unlock the door.

secret_code = input("enter the secret code:")
if secret_code == 1902873:
    print("Door unlocked.")
else:
    print("Incorrect code. Access denied.")
