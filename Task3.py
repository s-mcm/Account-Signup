import random


# Write your function below for guess_my_number 
def guess_my_number():
    attempts = 0

    print("Think of any number you want.")
    while True:
        try:
            lower_range = int(input("Enter the lower range that the number is in: "))
            break
        except ValueError:
            print("Enter a valid number.")
            continue

    while True:
        try:
            higher_range = int(input("Enter the higher range that the number is in: "))
            break
        except ValueError:
            print("Enter a valid number.")
            continue

    while True:
        # Guess a number that is exactly halfway between the ranges. This allows us to eliminate half
        # of the potential options in one guess
        guess = (lower_range + higher_range) // 2

        print(f"My guess is {guess}.\nIs this your number, higher or lower?")

        user_input = input('''Input "correct", "higher" or "lower": ''')

        if user_input == "correct":
            print(f"It took {attempts} guesses to find your number.")
            break
        elif user_input == "higher":
            # Change lower range to the guess value + 1 as we now know that the number is higher than the current guess
            lower_range = guess + 1
            attempts += 1
        elif user_input == "lower":
            # Change higher range to the guess value as we now know that the number is lower than the current guess
            higher_range = guess
            attempts += 1
        else:
            print("Invalid input.")


# Program main -- Do not change code below
guess_my_number()
