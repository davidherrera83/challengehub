import random

def guessing_game(low: int = 1, high: int = 10, max_tries: int = 3) -> None:
    """
    Number Guessing Game

    Description:
    A simple console-based game where the computer selects a random number
    between `low` and `high` (inclusive), and the player has `max_tries` attempts
    to guess the number. Feedback is provided after each guess to indicate whether
    the guess was too low or too high.

    Notes:
    - Invalid inputs (non-integer values) do not count as attempts.
    - The game ends when the player guesses the number or exhausts all attempts.
    - The function prints the outcome of the game to the console.

    Parameters:
    - low (int): The lower bound of the range (inclusive).
    - high (int): The upper bound of the range (inclusive).
    - max_tries (int): The maximum number of attempts allowed.
    """
    secret = random.randint(low, high)
    print(f"I've picked a number between {low} and {high}.")
    print(f"You have {max_tries} attempts to guess it.")

    for attempt in range(1, max_tries + 1):
        try:
            guess = int(input(f"\nAttempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if guess == secret:
            print(f"Correct! You guessed the number in {attempt} attempts.")
            return
        elif guess < secret:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")

    print(f"Game over. The correct number was {secret}.")

if __name__ == "__main__":
    guessing_game()