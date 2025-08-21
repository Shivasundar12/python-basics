# return → Exit from a function
# Stops the function immediately and optionally sends a value back to the caller.

# It can be used inside loops too — but only if the loop is inside a function.

# What it does: Immediately stops the function and sends a value back to the caller.

# Where it works: only inside a function.



# Example of using return in a function


def check_number(num):
    if num > 0:
        print("The number is positive.")
        if num % 2 == 0:
            return "It is also even."
        else:
            return "It is also odd."
    else:
        return "The number is not positive."




def find_first_even(nums):
    for n in nums:
        if n % 2 == 0:
            return n     # returns immediately when first even is found
    return None

print(find_first_even([1, 3, 5, 7,14 ]))  





