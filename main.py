import random


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"

    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"

    return "computer"


def display_score(user_score, computer_score, ties):
    print("\n---------- SCORE ----------")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")
    print("---------------------------")


def play_game():
    user_score = 0
    computer_score = 0
    ties = 0

    choices = {
        "1": "rock",
        "2": "paper",
        "3": "scissors"
    }

    print("\n========================================")
    print("       ROCK PAPER SCISSORS")
    print("========================================")

    while True:
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        print("4. Quit")

        user_input = input("\nEnter your choice: ").strip()

        if user_input == "4":
            break

        if user_input not in choices:
            print("❌ Invalid choice! Please choose 1, 2, 3, or 4.")
            continue

        user_choice = choices[user_input]
        computer_choice = get_computer_choice()

        print(f"\nYou chose: {user_choice.title()}")
        print(f"Computer chose: {computer_choice.title()}")

        result = determine_winner(user_choice, computer_choice)

        if result == "user":
            print("🎉 You Win!")
            user_score += 1

        elif result == "computer":
            print("😔 Computer Wins!")
            computer_score += 1

        else:
            print("🤝 It's a Tie!")
            ties += 1

        display_score(user_score, computer_score, ties)

    print("\n========================================")
    print("             FINAL SCORE")
    print("========================================")

    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    print(f"Ties: {ties}")

    if user_score > computer_score:
        print("🏆 You won the game!")

    elif computer_score > user_score:
        print("💻 Computer won the game!")

    else:
        print("🤝 The game ended in a tie!")

    print("\nThanks for playing! 👋")


def main():
    play_game()


if __name__ == "__main__":
    main()
