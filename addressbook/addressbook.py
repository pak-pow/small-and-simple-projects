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

        name = input("Enter Name: ")
        gender = input("Enter gender: ")
        age = input("Enter Age: ")
        city = input("Enter City: ")
        street = input("Enter Street: ")
        phone = input("Enter Phone Number: ")

        self.append_input(name, gender, age, city, street, phone)


if __name__ == "__main__":
    app = AddressBook()
    app.run()
