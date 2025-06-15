import csv
import os


class AddressBook:

    FILENAME = "addressbook.csv"
    ROW_HEADER = ["Name", "Gender", "Age", "City", "Street", "Phone Number"]

    def init_file(self):

        with open(self.FILENAME, "w", newline = "") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(self.ROW_HEADER)


    def append_input(self):

        name = input("Enter Name: ").title().strip()
        gender = input("Enter Gender: ").title().strip()

        while True:

            try:
                age = int(input("Enter Age: "))
                break

            except ValueError:
                print("Invalid Input, Try Again")

        city = input("Enter City: ").title().strip()
        street = input("Enter Street: ").title().strip()
        phone = input("Enter Phone Number: ").strip()

        result = [name,gender,age,city,street,phone]

        with open(self.FILENAME, "a", newline = "") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(result)

    def update(self):

        name_to_update = input("Enter the name you want to update: ").title().strip()
        updated_rows = []
        matches = []

        # Step 1: Load all rows
        with open(self.FILENAME, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                updated_rows.append(row)

                if name_to_update.lower() in row["Name"].lower(): # <----- getting all the name even if partially
                    matches.append(row)

        # Step 2: If no match found
        if not matches:
            print(f"No records found for name: {name_to_update}")
            return

        # Step 3: Show all matches with indexes

        print("\nMatches found:")

        print("--" * 59)
        print(f"[INFO  ]:\t\t| {'NAME':<25} | {'GENDER':<6} | {'AGE':<3} | {'CITY':<14} | {'STREET':<25} | {'PHONE NUMBER':<12} |")
        print("--" * 59)

        for idx, r in enumerate(matches, start=1):
            print(f"[INFO  ]:\t{idx}.) | {r['Name']:<25} | {r['Gender']:<6} | {r['Age']:<3} | {r['City']:<14} | {r['Street']:<25} | {r['Phone Number']:<12} |")
        print("--" * 59)

        # Step 4: Let user choose which one to update

        while True:
            try:

                selected = int(input("Enter the number of the record to update: "))

                if 1 <= selected <= len(matches):
                    break
                else:
                    print("Invalid selection.")

            except ValueError:
                print("Please enter a valid number.")

        selected_row = matches[selected - 1]

        # Step 5: Get new data

        print("\nEnter new values (leave blank to keep current):")

        new_gender = input(f"Gender ({selected_row['Gender']}): ").title().strip()     or selected_row["Gender"]
        new_age =    input(f"Age ({selected_row['Age']}): ").strip()                   or selected_row["Age"]
        new_city =   input(f"City ({selected_row['City']}): ").title().strip()         or selected_row["City"]
        new_street = input(f"Street ({selected_row['Street']}): ").title().strip()     or selected_row["Street"]
        new_phone =  input(f"Phone Number ({selected_row['Phone Number']}): ").strip() or selected_row["Phone Number"]

        # Step 6: Update only the selected row

        for row in updated_rows:

            if row == selected_row:

                row["Gender"] = new_gender
                row["Age"] = new_age
                row["City"] = new_city
                row["Street"] = new_street
                row["Phone Number"] = new_phone

                break

        # Step 7: Save everything

        with open(self.FILENAME, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.ROW_HEADER)
            writer.writeheader()
            writer.writerows(updated_rows)

        print("Address successfully updated.")

    def list(self):

        with open(self.FILENAME, "r", newline = "") as csv_file:
            readers = csv.DictReader(csv_file)

            print("--" * 59)
            print(f"[INFO  ]:\t| {'NAME':<26} | {'GENDER':<6} | {'AGE':<3} | {'CITY':<14} | {'STREET':<25} | {'PHONE NUMBER':<12} |")
            print("--" * 59)

            for r in readers:
                print(f"[INFO  ]:\t| {r['Name']:<26} | {r['Gender']:<6} | {r['Age']:<3} | {r['City']:<14} | {r['Street']:<25} | {r['Phone Number']:<12} |")
            print("--" * 59)

    def delete(self):
        name_to_delete = input("Enter the name you want to delete: ").title().strip()
        all_rows = []
        matches = []
        match_indexes = []

        # Step 1: Read all rows
        with open(self.FILENAME, "r", newline="") as csv_file:
            reader = csv.DictReader(csv_file)

            for idx, row in enumerate(reader):
                all_rows.append(row)

                if name_to_delete.lower() in row["Name"].lower():
                    matches.append(row)
                    match_indexes.append(idx)  # Save index of match in all_rows

        # Step 2: No matches
        if not matches:
            return print(f"No records found for name: {name_to_delete}")

        # Step 3: Display matches
        print("\nMatches found:")

        print("--" * 59)
        print(f"[INFO  ]:\t\t| {'NAME':<25} | {'GENDER':<6} | {'AGE':<3} | {'CITY':<14} | {'STREET':<25} | {'PHONE NUMBER':<12} |")
        print("--" * 59)

        for idx, r in enumerate(matches, start=1):

            print(f"[INFO  ]:\t{idx}.) | {r['Name']:<25} | {r['Gender']:<6} | {r['Age']:<3} | {r['City']:<14} | {r['Street']:<25} | {r['Phone Number']:<12} |")

        print("--" * 59)

        # Step 4: Ask which one to delete

        while True:
            try:
                selected = int(input("Enter the number of the record to delete: "))

                if 1 <= selected <= len(matches):
                    break

                else:
                    print("Invalid selection.")

            except ValueError:
                print("Please enter a valid number.")

        # Step 5: Delete the row by index in all_rows
        delete_index = match_indexes[selected - 1]
        deleted_row = all_rows.pop(delete_index)

        # Step 6: Write remaining rows back
        with open(self.FILENAME, "w", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=self.ROW_HEADER)
            writer.writeheader()
            writer.writerows(all_rows)

        print(f"[INFO  ]:\t{selected}.) | {deleted_row['Name']:<25} | {deleted_row['Gender']:<6} | {deleted_row['Age']:<3} | {deleted_row['City']:<14} | {deleted_row['Street']:<25} | {deleted_row['Phone Number']:<12} |")
        print(f"[INFO  ]:\tRow {selected}.) Has Been Deleted, Row Name: {deleted_row['Name']}")

    def search_loc(self):

        get_loc = input("Enter City: ").title().strip()

        with open(self.FILENAME, "r", newline = "") as csv_file:
            reader = csv.DictReader(csv_file)
            records = list(reader)

        matches = [x for x in records if x["City"] == get_loc]

        if matches:

            print("\nMatches found:")
            print("--" * 59)
            print(f"[INFO  ]:\t\t| {'NAME':<25} | {'GENDER':<6} | {'AGE':<3} | {'CITY':<14} | {'STREET':<25} | {'PHONE NUMBER':<12} |")
            print("--" * 59)

            for idx, i in enumerate(matches, start=1):
                print(f"[INFO  ]:\t{idx}.) | {i['Name']:<25} | {i['Gender']:<6} | {i['Age']:<3} | {i['City']:<14} | {i['Street']:<25} | {i['Phone Number']:<12} |")
            print("--" * 59)

        else:
            print(f"No records found for city: {get_loc}")

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
            "5" : "Search Address By Location",
            "6" : "Exit",

        }

        for idx, x in choices.items():
            print (f"\t{idx}.) {x}")

        while True:

            try:

                player_choice = int(input("\nEnter choice: "))

                if player_choice == 1:
                    self.append_input()

                elif player_choice == 2:
                    self.list()

                elif player_choice == 3:
                    self.update()

                elif player_choice == 4:
                    self.delete()

                elif player_choice == 5:
                    self.search_loc()

                elif player_choice == 6:
                    break

                if input("Would you like to go back to menu?(Y/N): ").lower() != "y": break


            except ValueError:
                print("Invalid Input, Try Again.")

if __name__ == "__main__":
    app = AddressBook()
    app.run()
