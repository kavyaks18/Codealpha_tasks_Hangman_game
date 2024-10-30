import random

# List of possible words for the Hangman game
words = ['python', 'developer', 'hangman', 'programming', 'algorithm', 'function', 'variable']

# Function to choose a random word from the list
def get_random_word(words):
    return random.choice(words).lower()

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    display = [letter if letter in guessed_letters else '_' for letter in word]
    return ' '.join(display)

# Hangman game function
def hangman():
    word = get_random_word(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit of incorrect guesses

    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")

    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + display_word(word, guessed_letters))
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

        # Input validation: make sure the player enters a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        # If the guessed letter is correct
        if guess in word:
            if guess not in guessed_letters:
                guessed_letters.append(guess)
                print(f"Good guess! '{guess}' is in the word.")
            else:
                print(f"You already guessed '{guess}'.")
        else:
            # If the guessed letter is incorrect
            incorrect_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.")

        # Check if all letters in the word are guessed
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nYou've run out of guesses. The word was: {word}. Better luck next time!")

# Start the game
if __name__ == "__main__":
    hangman()
