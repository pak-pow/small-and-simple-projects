import random

def game_function(get_user_input, life, score):

    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)


    if get_user_input == computer_choice:
        print("Result: DRAW!")

    elif get_user_input == "rock" and computer_choice == "paper":
        life -= 1
        print (f"Result: YOU LOSE! your choice: {get_user_input}, computer choice: {computer_choice}")

    elif get_user_input == "paper" and computer_choice == "rock":
        score += 1
        print (f"Result: YOU WON! your choice: {get_user_input}, computer choice: {computer_choice}")

    elif get_user_input == "rock" and computer_choice == "scissors":
        score += 1
        print (f"Result: YOU WON! your choice: {get_user_input}, computer choice: {computer_choice}")

    elif get_user_input == "scissors" and computer_choice == "rock":
        life -= 1
        print (f"Result: YOU LOSE! your choice: {get_user_input}, computer choice: {computer_choice}")

    elif get_user_input == "scissors" and computer_choice == "paper":
        score += 1
        print (f"Result: YOU WON! your choice: {get_user_input}, computer choice: {computer_choice}")

    elif get_user_input == "paper" and computer_choice == "scissors":
        life -= 1
        print (f"Result: YOU LOSE! your choice: {get_user_input}, computer choice: {computer_choice}")

    return life, score


def main():

    print("\n\t Welcome to Rock, Paper, Scissors Game!\n")
    print("========" * 6)
    print("\t\t\t |ROCK|PAPER|SCISSORS|\n")

    choices = ["rock", "paper", "scissors"]

    while True:
        life = 3
        score = 0

        while life > 0:

            try:

                print("--------" * 6)
                print (f"Remaining Life: {life} | Score: {score}")
                get_user_input = input("Please enter your choice: ").lower().strip()
                print ("--------" * 6)

                if get_user_input not in choices:
                    raise ValueError ("Invalid Input, Please correct your input")

                life, score = game_function(get_user_input, life, score)

            except ValueError as e:
                print(e)

        print ("========" * 6)
        print ("")
        print (f"Game Over! You've run out of lives | SCORE: {score}")
        print ("")
        print ("========" * 6)

        play_again = input("Would you like to try again?(y/n): ").lower().strip()

        if play_again not in ["yes", "y"]:
            print("Thanks for playing!, Goodbye.")
            break


if __name__ == "__main__":
    main()