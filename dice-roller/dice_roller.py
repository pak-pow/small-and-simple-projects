import random
import time

def get_dice(user_choice = None):

    dices = {

        "D4": 4,
        "D6": 6,
        "D10": 10,
        "D12": 12,
        "D20": 20

        }

    return list(range(1, dices[user_choice] + 1))

if __name__ == "__main__":

    print ("")
    print ("======" * 6)
    print ("\n\t  Welcome to Dice Roller!\n")
    print ("======" * 6)

    print ("\n\t\t\t  |DICES|")
    print ("\t\t|D4|D6|D10|D12|D20|")

    choices = ["D4", "D6", "D10", "D12", "D20"]

    while True:
        get_user_input = input("\nDice: ").upper().strip()

        if get_user_input not in choices:
            print("Invalid Input, Try Again.")
            continue

        print(f"You picked {get_user_input} with sides {get_dice(get_user_input)}")
        time.sleep(1)

        print("Rolling...")
        time.sleep(2)

        result = random.choice(get_dice(get_user_input))
        print(f"You got... {result}")

        print("------" * 6)
        try_again = input("Would you like to try again (y/n)?: ").strip().lower()
        print("------" * 6)

        if try_again != "y":
            print("Thanks for playing! Come Again!")
            break
