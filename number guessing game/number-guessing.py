# Made by Vee / Me

import random

print ("\t Welcome to Number Guessing game!")
print ("=======" * 6)

hearts = 3

while True:

    computer_guess = random.randint(1,10)

    print(f"\nRemaining Life: {hearts}")

    try:
        get_user_input = int(input("Please enter a number (1-10): "))

    except ValueError:

        print("Invalid input! Please enter a number.")
        continue
    if get_user_input == computer_guess:

        print ("-------" * 6 )
        print(f"You won! your guess: {get_user_input}, computer guess: {computer_guess}")
        print ("-------" * 6 )

        ta = input("Would you like to try again?(y/n): ").strip().lower()

        if ta == "y":
            hearts = 3

        else:
            print("-------" * 6)
            print("Thanks For Playing!!")
            print("-------" * 6)
            break

    elif get_user_input != computer_guess:
        hearts -= 1

        if hearts >= 1:

            response = [

                "Opps, try again",
                "Haha, wrong. Try again",
                "Wow, is that how you guess?",
                "Geez, you guessed it wrong",
                "WOW, nah u wrong",

                ]

            random_response = random.choice(response)

            print ("-------" * 6)
            print(random_response)
            print ("-------" * 6)

        elif hearts == 0:

            print ("-------" * 6)
            print("You lost :<")
            print ("-------" * 6)

            ta = input("Would you like to try again?(y/n): ").strip().lower()

            if ta == "y":
                hearts = 3

            else:
                print("-------" * 6)
                print("Thanks For Playing!!")
                print("-------" * 6)
                break
