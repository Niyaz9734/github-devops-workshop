print ("hello world how are you")
print ("I am fine,thanks")

# 1. Defining a Function
def greet_user(username, user_age):
    """This function takes a name and age, prints a greeting, 
    and checks if the user is an adult."""
    print(f"\n--- Welcome, {username}! ---")
    
    # 2. Conditional Logic (if/else)
    if user_age >= 18:
        print("Status: Access granted to adult dashboard.")
    else:
        years_left = 18 - user_age
        print(f"Status: Limited access. Come back in {years_left} years!")

# 3. Handling User Input
print("=== Python Core Demo ===")
name = input("Enter your name: ")

# We convert the input string to an integer using int()
age = int(input("Enter your age: "))

# 4. Calling the Function
greet_user(name, age)

