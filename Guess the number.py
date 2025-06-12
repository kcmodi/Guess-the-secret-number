#
# SEC290.32327.B2.SUM2023
# Kalpen Modi
# 07/21/2023
# Hwk #3

import random
def secret_number_game():
    # Generate the secret number
    secret = random.randint(1, 20)

    print("Guess the secret number!\nYou start out with 3 lives and you lose one with each wrong guess.")

    # Initialize the number of lives
    num_lives = 3
    # Start the game loop
    while num_lives > 0:
        # Ask the user for a guess
        guess = int(input("Please guess your number between 1 and 20: "))

        # Check if the guess is greater than the secret
        if guess > secret:
            print("Too high!")
        # Check if the guess is less than the secret
        elif guess < secret:
            print("Too low!")
        # If neither greater nor less, the guess is correct
        else:
            print(f"Congratulations! You guessed the secret number, {secret}!")
            break

        # Decrement the number of lives and display the remaining lives
        num_lives -= 1
        if num_lives > 0:
            print(f"Lives remaining: {num_lives}")

    # Check if the user has run out of lives
    if num_lives == 0:
        print(f"You lost! The secret number was {secret}.\nBetter luck next time!")

# Call the function to play the game
secret_number_game()