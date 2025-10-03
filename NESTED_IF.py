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
        if adult_accompany == "yes":
            print("You can watch the movie.")
        else:
            print("You cannot watch the movie without an adult.")
    else:
        print("You can watch the movie.")


# Problem 1: Concert Ticket Access
# Scenario: A concert is for adults (18+). Furthermore, to enter the VIP section, you must also have a VIP pass.
# Logic:
# First, check if the person is an adult.
# If they are, then check if they have a VIP pass.
# If they do, grant VIP access.

age = int(input("Enter your age: "))
vip_pass = input("Do you have a VIP pass? (yes/no): ").lower() == 'yes'

if age >=18:
    print("You are a adult and allowed to enter the concert")
    if vip_pass:
        print("You have a VIP pass and can enter the VIP section.")
    else:
        print("You do not have a VIP pass and cannot enter the VIP section.")
else:
    print("You are not an adult and cannot enter the concert.")


# Problem 2: Online Purchase Approval
# Scenario: An online store requires a purchase to be over $50 for free shipping. Additionally, the item must be in stock.

# Logic:
# First, check if the cart total is over $50.
# If it is, then check if the item is in stock.
# If it is, offer free shipping.

cart_total = float(input("Enter your cart total: $"))
in_stock = input("Is the item in stock? (yes/no): ").lower() == 'yes'
if cart_total >= 50:
    print("your products are available for free shipping!")
    if in_stock:
        print("The item is in stock. You can proceed to checkout with free shipping.")
    else:
        print("The item is not in stock. Please check back later.")
else:
    print("Your cart total is less than $50. Free shipping is not available.")



# Problem 3: Weather-appropriate Clothing Advisor
# Create a program that gives clothing advice based on the weather:
# If the temperature is below 50°F, advise to "Wear a jacket."
# If it's also raining, advise to "Bring an umbrella."
# If the wind_speed is over 15 mph, add "Make it a strong umbrella!"
# If it's not raining but the temperature is below 32°F, advise to "Wear heavy gloves and a hat."
# If the temperature is 50°F or above, advise "Light clothing should be fine."
# Use the variables temperature, is_raining, and wind_speed.

temperature = float(input("Enter the temperature in °F: "))
is_raining = input("Is it raining? (yes/no): ").lower() == 'yes'
wind_speed = float(input("Enter the wind speed in mph: "))
if temperature < 50:
    print("wear a jacket")
    if is_raining:
        print("bring an umbrella")
        if wind_speed > 15:
            print("make it a strong umbrella!")
        elif temperature < 32:
            print("wear heavy gloves and a hat")
else:
    print("light clothing should be fine")


# Problem 4: College Admission Chance Estimator
# A university estimates admission chances based on:
# First, a GPA of at least 3.5 is required.
# If GPA is sufficient, an SAT score of at least 1300 is required for a strong chance.
# If the student also has a strong letter of recommendation, they are "Likely accepted."
# If not, their application is "Under review."
# If the GPA is sufficient but the SAT score is between 1200 and 1299, the application is "Borderline... will be reviewed."
# If the GPA is sufficient but the SAT is below 1200, the score is "too low."
# If the GPA is below 3.5, the applicant does "not meet minimum requirements."
# Use gpa, sat_score, and has_recommendation variables. Print the admission status.



gpa = float(input("Enter your GPA: "))
sat_score = int(input("Enter your SAT score: "))
has_recommendation = input("Do you have a strong letter of recommendation? (yes/no): ").lower() == 'yes'
if gpa >= 3.5:
    print("you have sufficient GPA")
    if sat_score >=1300:
        if has_recommendation:
            print("likely accepted")
        else:
            print("under review")
    elif 1200 <= sat_score < 1300:
        print("borderline... will be reviewed")
    else:
        print("your SAT score is too low")
else:
    print("you do not meet minimum requirements")






