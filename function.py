# what is functions! in python!
# Think of a function like a kitchen appliance - let's say a blender:
# You put ingredients in (INPUT)
# It does some work (PROCESSING)
# It gives you a smoothie out (OUTPUT)
# You don't need to know HOW the blender works internally - you just need to know WHAT it does!

# def function_name(parameters):
#     """docstring - explains what the function does"""
#     # code that does something
#     return result



# 🟢 1. Why do we use print()?
# Purpose: To show information on the screen for the user (output, debugging, progress).
# Think of it like speaking aloud 📢 — the program tells you something.
def greet(name):
    print("Hello", name)

greet("Shiva")




# 🔵 2. Why do we use return?
# Purpose: To send a value back to the program so you can use it later.
# Think of it like handing you an object 🎁 — you can save it, use it in math, pass it to another function, etc.
def add (a, b):
    return a + b
result = add(3, 4)  # result now holds the value 7
print("Result from return function:", result)  # This will print 7 because add()
    

#     🧠 Simple Analogy:
# print → showcase window in a pizza shop 🍕 (you see it but can’t take it home).
# return → pizza packed in a box 📦 (you can take it, store it, eat it later, give it to others).

