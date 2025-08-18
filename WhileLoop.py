# what is while loop?
# A while loop is used to execute a block of code repeatedly as long as a specified condition is true.
# With the while loop we can execute a set of statements as long as a condition is true.
# NOTE: remember to increment i, or else the loop will continue forever.



# 📝 Problem:

# Write a Python program using a while loop that:
# Starts from 1
# Prints all numbers up to 20
# But skips multiples of 4
# And stops completely when it reaches 15

i = 0
while i <=20:
    i += 1  
    if i % 4 == 0:
        continue
    print(i)
    if i == 10:
        break

# 🚀 Problem:
# Write a program using a while loop that:
# Starts from i = 50 and counts down to 1.
# Skips numbers that are divisible by 5.
# Stops completely if it reaches 13.
# Prints only the allowed numbers.

i = 50
while i >= 1:
    if i % 5 == 0:
        i -=1
        continue
    if i == 13:
        break
    print(i)
    i -= 1



# 📝 Problem:
# Write a program using a while loop that:
# Starts from number 1.
# Keeps adding numbers (sum) until the total sum reaches or exceeds 100.
# Print the final sum and how many numbers were added.

sum = 0
count = 0
i = 1
while sum < 100:
    sum += i
    count += 1
    i += 1
    print("Final Sum:", sum)  
print("Numbers Added:", count)


n = 10

while n > 0:
    print(n)
    n -= 1
    if n == 5:
        continue
    if n == 2:
        break