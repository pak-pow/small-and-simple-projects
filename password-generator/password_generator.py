# Made by Vee / Me

import string
import secrets

def make_password(length=0, charac=None, number=None, special_charac=None):
    character = ''

    if charac:
        character += string.ascii_letters

    if number:
        character += string.digits

    if special_charac:
        character += string.punctuation

    if not character:
        print("Nothing selected, try again.")
        return None

    password = ''.join(secrets.choice(character) for _ in range(length))

    return password

def main():
    print("\t  Welcome to Password Generator!")
    print ("-------" * 6)

    while True:

        try:
            length = int(input("Enter Password Length: "))

        except ValueError:
            print ("Invalid Input, Try again.")
            continue

        charac = input("Include Letters? (y/n): ").lower() == 'y'
        number = input("Include Digits? (y/n): ").lower() == 'y'
        special_charac = input("Include Symbols? (y/n): ").lower() == 'y'

        password = make_password(length, charac, number, special_charac)

        print ("=======" * 6)
        if password:
            print("Generated Password:", password)
        print ("=======" * 6)


        try_again = input("\n\tWould you like to try again?(y/n): ").lower().strip()
        print ("")
        print ("-------" * 6)
        if try_again == "y":
            continue

        else:
            print("")
            print("\tThank you for using this program!")
            print("")
            print ("-------" * 6)
            break

if __name__ == "__main__":
    main()
