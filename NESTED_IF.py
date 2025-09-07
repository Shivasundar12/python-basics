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



