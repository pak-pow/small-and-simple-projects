import csv
import os
import random

FILENAME = "questions.csv"
headers = ["Question", "Option A", "Option B","Option C","Option D", "Answer"]


def create_file():

    # Creating a New file in csv if there is none

    with open(FILENAME, "w", newline = "") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(headers)

def load_question():

    # Storing Questions

    question = []

    with open(FILENAME, "r", newline = "") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            question.append({
                "Question" : row["Question"],
                "Options" : [row["Option A"], row["Option B"], row["Option C"], row["Option D"]],
                "Answer" : row["Answer"]
            })
    return question

def load_quiz(question):

    score = 0
    random.shuffle(question)

    for index, q in enumerate(question, start = 1):
        print (f"\nQ{index}: {q["Question"]}\n")
        options = q["Options"]
        random.shuffle(options)

        for idx, o in enumerate(options, start = 1):
            print(f"\t{idx}.{o}")

        try:
            get_user_input = int(input("\n  Your Answer(1-4): "))

            if options[get_user_input - 1] == q["Answer"]:
                print("  ✅ Correct!")
                score += 1

            else:
                print(f"  ❌ Wrong! Correct answer was: {q['Answer']}")

        except (ValueError, IndexError):
            print("Invalid input. Moving to next question.")

    print(f"\nFinal Score: {score}/{len(question)}")


if __name__ == "__main__":

    if not os.path.exists(FILENAME):
        create_file()

    else:
        pass

    load_quiz(load_question())

