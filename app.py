import random

import analyticskit
import analyticskit.analyticskit as _ak
from analyticskit import single_input

# --- Fix for newer Tk (9.x) on Mac ---
# analyticskit's show_message() crashes when width is small (the default is 0)
# because Tk 9 rejects the negative text-wrap width it computes.
_original_show_message = _ak.show_message


def show_message(title, message, width=0, height=0):
    _original_show_message(title, message, width=max(width, 300), height=height)


_ak.show_message = show_message
analyticskit.show_message = show_message


def main():
    while True:

        secret_number = random.randint(1, 10)

        guess = single_input("Guess a number between 1 and 10.")

        try:
            guess = int(guess)
        except (TypeError, ValueError):
            show_message("Invalid guess", f"That wasn't a whole number. The correct number was {secret_number}.")
            guess = None

        if guess == secret_number:
            show_message("You win!", "You win! You guessed the correct number.")
        elif guess is not None:
            show_message("You lose", f"You lose. The correct number was {secret_number}.")

        play_again = single_input("Would you like to play again? Enter y/n.")

        if not play_again or play_again.strip().lower() != "y":
            break


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise
    except Exception:
        import traceback
        show_message("Unexpected error", traceback.format_exc())
