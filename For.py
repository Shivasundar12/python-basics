# what is for loop?
# A for loop is a control flow statement that allows code to be executed repeatedly based on a condition or over a sequence (like a list, tuple, or string).
# excute a code fixed number of times. you can iterate over string,list,tuple,dictionary, set
# there are two types of for loop in python:
# 1. for loop with range function
# 2. for loop with iterable objects (like lists, tuples, strings, etc.)
# for has some built-in functions (range,enumurate,len,zip,sorted,filter,map)


# program to demonstrate for loop with range function
# mulitiplication using for loop
# num = 5

# for i in range(1, 11):   # loop from 1 to 10
#     print(f"{num} x {i} = {num * i}")


nums = [2, 3, 4, 5]
result = 1

for n in nums:
    result *= n   # same as result = result * n

# print("Product =", result)

for i in reversed(range(1, 11)):
    print(i)
# print("happy new year")

# this is enumerate function

name = ["John", "Jane", "Doe"]
for i,j in enumerate(name):
    print(f"Index: {i}, Name: {j}")

# this is zip function
names = ["John", "Jane", "Doe"]
ages = [25, 30, 22]
area = ["rameshwaram", "karaikudi", "chennai"]

for names,age,area in zip(names, ages, area):
    print(f"Name: {names}, Age: {age}, Area: {area}")


nums = [1,2,34,83,41,98,0]

for n in sorted(nums):
    print(n)