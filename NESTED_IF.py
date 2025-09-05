# # Program to demonstrate nested if statements

# num = int(input("Enter a number: "))

# if num > 0:
#     print("The number is positive.")
#     if num % 2 == 0:
#         print("It is also even.")
#     else:
#         print("It is also odd.")
# else:
#     print("The number is not positive.")

# age = 20
# citizen = False

# if age >= 18:                 # Stage 1: Age check
#     print("You are an adult.") # Action 1
#     if citizen:               # Stage 2: Citizenship check
#         print("You can vote!") # Action 2
#     else:
#         print("But you are not a citizen, so you cannot vote.") # Different action
# else:
#     print("You are not an adult.") # Action if Stage 1 fails


# Odd or Even

num1 = int(input(("enter a number: ")))

if  num1 % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")



# Problem 1: The Movie Theater
# Scenario: A movie theater has the following rules:

# You must be 13 or older to watch a PG-13 movie.

# If you are under 16, you must be accompanied by an adult (over 18) for any movie after 8 PM.

age = int(input("Enter your age: "))
time = int(input("Enter the movie time (in 24-hour format): "))
adult_accompany = input("Are you accompanied by an adult? (yes/no): ").lower() == 'yes'

if age >=13:
    if time >20 and age <16:
        print("You need to be accompanied by an adult to watch this movie.")
        if adult_accompany == yes:
            print("You can watch the movie.")
        else:
            print("You cannot watch the movie without an adult.")
    else:
        print("You can watch the movie.")


        