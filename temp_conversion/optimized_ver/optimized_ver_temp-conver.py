def function(get_user_input, get_user_choice):

    conversions = {

        "1": (lambda x: x * 9 / 5 + 32, "°F"),                    # Celsius to Fahrenheit
        "2": (lambda x: (x - 32) * 5 / 9, "°C"),                  # Fahrenheit to Celsius
        "3": (lambda x: x + 273.15, "K"),                         # Celsius to Kelvin
        "4": (lambda x: x - 273.15, "°C"),                        # Kelvin to Celsius
        "5": (lambda x: (x - 32) * 5 / 9 + 273.15, "K"),          # Fahrenheit to Kelvin
        "6": (lambda x: (x - 273.15) * 9 / 5 + 32, "°F")          # Kelvin to Fahrenheit
    }

    if get_user_choice in conversions:

        formula, unit = conversions[get_user_choice]
        result = formula(get_user_input)

        print(f"Output: {result:.2f}{unit}")

    else:
        print("Invalid choice.")

def main():
    
    print("\nWelcome to Temperature Converter\n")
    print("\t1. Celsius -> Fahrenheit")
    print("\t2. Fahrenheit -> Celsius")
    print("\t3. Celsius -> Kelvin")
    print("\t4. Kelvin -> Celsius")
    print("\t5. Fahrenheit -> Kelvin")
    print("\t6. Kelvin -> Fahrenheit")

    while True:
        get_user_choice = input("\nEnter choice: ").strip()

        try:
            raw_input = input("Enter the temperature: ").strip("°F,°C,K,°")
            get_user_input = float(raw_input)
            function(get_user_input, get_user_choice)
        except ValueError:
            print("Please enter a valid number.")

        try_again = input("Try Again (y/n)?: ").strip().lower()
        if try_again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()