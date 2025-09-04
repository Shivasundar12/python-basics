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

# this function does not return anything explicitly
# so it returns None by default
def print_square(x):
    print(x * x)

# result = print_square(4)  # prints 16
# print("Result:", result)  # prints "Result: None"


# multiple return statements
def odd_even_checker(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
    print("This won't print")  # unreachable code
# print(odd_even_checker(10))  # prints "Even"
# print(odd_even_checker(7))   # prints "Odd"

# Returning Multiple Values


def calculate_stats(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average  # returns a tuple
stats = calculate_stats([10, 20, 30, 40])
print(stats)


# early return to avoid deep nesting
def validate_email(email):
    if "@" not in email:
        return "Invalid email: missing '@'"
    if "." not in email.split("@")[1]:
        return "Invalid email: missing domain"
    
    return True
print(validate_email("shiva3sundar@gmail.com"))
print(validate_email("invalidemail.com"))

# real-world example

# user authetication function
def authenticate(username, password, DB):
    if username not in DB:
        return "Username not found"
    if DB[username] != password:
        return "Incorrect password"
    return "Login successful"
# mock database
mock_db = { 
    'alice': {'password': 'shiva3sundar', 'is_active': True, 'role': 'admin' },
    'carl': {'password': 'siva123', 'is_active': False, 'role': 'student' }
}

result = authenticate('alice', 'password123', mock_db)
print(result)  # prints "Login successful"


#  Banking: Transaction Validation

def validate_transaction(account_balence, amount, transaction_type):
    if amount <=0:
        return {"success": False , "message": "Amount must be positive"}
    if transaction_type == 'withdraw':
        if amount > account_balence:
            return {"success": False , "message": "Insufficient funds"}
        new_balance = account_balence - amount
    elif transaction_type == 'deposit':
        new_balance = account_balence + amount
    else:
        return {"success": False , "message": "Invalid transaction type"}
    return {"success": True, "new_balance": new_balance}

result = validate_transaction(1000, 500, 'withdraw')
print(result)  # prints "Insufficient funds"

# maximum of two numbers using return 
def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b
print(max_of_two(10, 20))  # prints 20


