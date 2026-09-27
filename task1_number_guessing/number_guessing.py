import random


def play_game():
    print("\n================================")
    print("      NUMBER GUESSING GAME")
    print("================================")
    print("I have selected a number between 1 and 100.")
    print("You have 7 attempts to guess it!\n")

    secret_number = random.randint(1, 100)
    attempts = 7

    for attempt in range(1, attempts + 1):

        while True:
            try:
                guess = int(input(f"Attempt {attempt}/7 - Enter your guess: "))

                if guess < 1 or guess > 100:
                    print("Please enter a number between 1 and 100.")
                else:
                    break

            except ValueError:
                print("Invalid input! Please enter a number.")

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number!")
            print(f"You found it in {attempt} attempt(s).")
            return

        elif guess > secret_number:
            print("Too High! Try a smaller number.")

        else:
            print("Too Low! Try a bigger number.")

        remaining = attempts - attempt
        print(f"Attempts left: {remaining}\n")

    print("\n❌ Game Over!")
    print(f"The secret number was: {secret_number}")


def main():
    while True:
        play_game()

        while True:
            again = input("\nDo you want to play again? (yes/no): ").lower()

            if again == "yes":
                break
            elif again == "no":
                print("\nThanks for playing! Goodbye 👋")
                return
            else:
                print("Please enter yes or no.")


if __name__ == "__main__":
    main()
