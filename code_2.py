from datetime import datetime

# Function to calculate age based on birth year
def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

# Get the user's birth year
try:
    birth_year = int(input("Enter your birth year (e.g., 1990): "))
    if birth_year > datetime.now().year:
        print("You entered a future year, please enter a valid birth year.")
    else:
        # Calculate and display the user's age
        age = calculate_age(birth_year)
        print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")

