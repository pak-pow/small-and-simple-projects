import csv

FILENAME = "sample_data.csv"

def get_email():

    emails = []

    with open(FILENAME, "r", newline = "") as csv_file:
        reader = csv.DictReader(csv_file)

        for x in reader:
            get = x["Email"]
            emails.append(get)

        for email in emails:
            print(email)

get_email()
