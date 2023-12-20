import random


def sch_register():
    while True:
        full_name = input("Please enter your full name: ")

        if any(characters.isdigit() for characters in full_name):
            # Name contains a number = invalid
            print("Please remove the numbers from your first or last name")
        elif not any(characters in " " for characters in full_name):
            # Check for a space within the name to ensure that a first and last name was entered
            print("Please enter a valid first and last name")
        else:
            # Valid name given, the loop can be exited
            break

    # Code to extract the first name
    # String is split on space; first entry for the first name
    full_name = full_name.split(" ")
    first_name = full_name[0]

    # Say Hello xx
    print(f"Hello {first_name}")

    # Ask the user to enter their age
    # Validate their age for registration
    # The loop continues to run until a valid input is given
    while True:
        try:
            age = int(input("Please enter your age: "))
        except ValueError:
            # Runs when a non-integer value is given
            print("Please enter a valid age.")
            continue
        if age < 11:
            print("Sorry, you are too young to be registered in the school.")
            continue
        elif age > 18:
            print("Sorry, you are too old to be registered in the school.")
            continue
        else:
            # Valid age given, the loop can be exited
            break

    # ...finish the task, keep the same commenting style
    birthday = input("Please enter your date of birth in the format dd/mm/yyyy: ")
    # String is split on "/"; third option is the year
    birth_year = birthday.split("/")[2]
    print(f"You were born in the year {birth_year}.")

    random_number = random.randrange(10, 99)
    # Find length of string array full_name. Use length to select last value
    last_name = full_name[len(full_name) - 1]
    email = first_name[0] + last_name + birth_year + str(random_number) + "@school.ac.uk"

    return email


def pwd_validate(pwd):
    # Validate the length of the password
    # Check if password is strong
    symbols = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '/', '@', ';',
               ':', '#', ',', '<', "'", '~', '?']

    while True:
        if not len(pwd) == 12:
            # Password is not 12 characters long = invalid
            print("Invalid password entered. Password must be 12 characters long.")
        elif not any(characters in symbols for characters in pwd):
            # Password does not contain a symbol = invalid
            print("Invalid password entered. Password must contain a symbol.")
        elif not any(char.islower() for char in pwd):
            # Password does not contain a lowercase character = invalid
            print("Invalid password entered. Password must contain a lowercase character.")
        elif not any(characters.isupper() for characters in pwd):
            # Password does not contain a uppercase character = invalid
            print("Invalid password entered. Password must contain a uppercase character.")
        elif not any(characters.isdigit() for characters in pwd):
            # Password does not contain a number = invalid
            print("Invalid password entered. Password must contain a number.")
        else:
            # Password is valid so the loop can be exited
            break

        # If this code is reached, the entered password was invalid. Ask for a new password to be validated
        pwd = input("\nPlease enter your new password, it should be 12 characters long: ")

    # ...finish the task and RETURN the right variable.
    print("Your new password is: ")

    return pwd


# Program main --- Do not change the code below but feel free to comment out 
# sections of code when working on individual functions. 
# Calling Task 1 function
email = sch_register()
print("Your new school email is: ", email)

# Calling Task 2 function
pwd = input("\nPlease enter your new password, it should be 12 characters long: ")
print("Your new password is: ")
print(pwd_validate(pwd))
