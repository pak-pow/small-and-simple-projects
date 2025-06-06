import random
from words import word_list


def get_word():
    return random.choice(word_list).upper()


def display_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[tries]


def update_word_completion(word, word_completion, guess):
    return ''.join([
        guess if word[i] == guess else word_completion[i]
        for i in range(len(word))
    ])


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("Word: " + word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").strip().upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already guessed the letter '{guess}'.")
            elif guess not in word:
                print(f"'{guess}' is not in the word.")
                tries -= 1
                guessed_letters.add(guess)
            else:
                print(f"Good job! '{guess}' is in the word!")
                guessed_letters.add(guess)
                word_completion = update_word_completion(word, word_completion, guess)
                if "_" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word '{guess}'.")
            elif guess != word:
                print(f"'{guess}' is not the word.")
                tries -= 1
                guessed_words.add(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Invalid guess. Please try again.")

        print(display_hangman(tries))
        print("Word: " + word_completion)
        print("\n")

    if guessed:
        print("🎉 Congrats, you guessed the word! You win!")
    else:
        print(f"😞 Sorry, you ran out of tries. The word was '{word}'. Better luck next time!")


def main():
    while True:
        word = get_word()
        play(word)
        replay = input("Play again? (Y/N): ").strip().upper()
        if replay != "Y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    main()
