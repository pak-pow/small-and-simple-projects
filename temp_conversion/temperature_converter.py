# making temperature converter
def function(get_user_input, get_user_choice):

    if get_user_choice == "1":

        formula = get_user_input * 9/5 + 32
        print (f"Output: {formula:.2f}°F")

    elif get_user_choice == "2":

        formula = (get_user_input - 32) * 5/9
        print (f"Output: {formula:.2f}°C")

    elif get_user_choice == "3":

        formula = get_user_input + 273.15
        print (f"Output: {formula:.2f}K")

    elif get_user_choice == "4":

        formula = get_user_input - 273.15
        print (f"Output: {formula:.2f}°C")

    elif get_user_choice == "5":

        formula = (get_user_input - 32) * 5/9 + 273.15
        print (f"Output: {formula:.2f}K")

    elif get_user_choice == "6":

        formula = (get_user_input - 273.15) * 9/5 + 32
        print (f"Output: {formula:.2f}°F")


def main():

    print ("\nWelcome to Temperature Converter\n")

    print ("\t1. Celsius -> Fahrenheit")
    print ("\t2. Fahrenheit -> Celsius")
    print ("\t3. Celsius -> Kelvin")
    print ("\t4. Kelvin -> Celsius")
    print ("\t5. Fahrenheit -> Kelvin")
    print ("\t6. Kelvin ->  Fahrenheit")

    while True:

        get_user_choice = input("\nEnter choice: ")

        try:
            get_user_input = float(input("Enter the temperature: ").strip("°F,°C,K,°"))
            function(get_user_input, get_user_choice)

        except ValueError:
            print("Please enter a valid number.")

        try_again = input("Try Again(y/n)?: ").strip().lower() == "y" or "Y"

        if try_again:
            continue

        else:
            break

if __name__ == "__main__":
    main()