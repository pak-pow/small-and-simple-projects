import csv
import os

class AddressBook:

    FILENAME = "addressbook.csv"
    ROW_HEADER = ["Name", "Gender", "Age", "City", "Street", "Phone Number"]

    def init_file(self):

        with open(self.FILENAME, "w", newline = "") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.ROW_HEADER)


    def append_input(self, name, gender, age, city, street, phone):

        result = [name,gender,age,city,street,phone]

        with open(self.FILENAME, "a", newline = "") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(result)

    def search_csv(self):
        pass

    def list(self):
        pass

    def delete(self):
        pass

   def run(self):

        if not os.path.exists(self.FILENAME):
            self.init_file()

        else:
            pass

        choices = {

            "1" : "Create Address",
            "2" : "Read / List All Address ",
            "3" : "Update Address By Name",
            "4" : "Delete Address By Name",
            "5" : "Search Address By Name",
            "6" : "Exit",

        }

        for idx, x in choices.items():
            print (f"\t{idx}.) {x}")

        try:

            player_choice = int(input("\nEnter choice: "))

            if player_choice == 1:

                name = input("Enter Name: ")
                gender = input("Enter gender: ")

                while True:

                    try:
                        age = int(input("Enter Age: "))
                        break

                    except ValueError:
                        print("Invalid Input, Try Again")

                city = input("Enter City: ")
                street = input("Enter Street: ")
                phone = input("Enter Phone Number: ")

                self.append_input(name, gender, age, city, street, phone)

            elif player_choice == "2":
                pass

            elif player_choice == "3":
                pass

            elif player_choice == "4":
                pass

            elif player_choice == "5":
                pass

            elif player_choice == "6":
                pass

        except ValueError:
            print("Invalid Input, Try Again.")
            
if __name__ == "__main__":
    app = AddressBook()
    app.run()
