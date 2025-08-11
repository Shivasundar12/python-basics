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