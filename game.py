import random


def hangman():
    # List of words to choose from
    word_list = ['python', 'hangman', 'challenge', 'developer', 'program']
    secret_word = random.choice(word_list).lower()
    guessed_letters = set()
    correct_letters = set(secret_word)
    max_attempts = 6
    attempts = 0

    print("Welcome to Hangman!")
    print("_ " * len(secret_word))

    while attempts < max_attempts and correct_letters != guessed_letters:
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts += 1

        # Show current progress
        display = [letter if letter in guessed_letters else '_' for letter in secret_word]
        print("Word: ", ' '.join(display))
        print(f"Remaining attempts: {max_attempts - attempts}")

    if correct_letters == guessed_letters:
        print(f"Congratulations! You guessed the word '{secret_word}'.")
    else:
        print(f"Game over! The word was '{secret_word}'.")

# Run the game
hangman()
