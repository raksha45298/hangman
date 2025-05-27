import random

# List of possible words
word_list = ['python', 'hangman', 'challenge', 'programming', 'developer', 'function', 'variable']

# Choose a random word
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Game settings
max_attempts = 6
guessed_letters = []
incorrect_guesses = 0
display = ['_'] * word_length

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Game loop
while incorrect_guesses < max_attempts and '_' in display:
    print("\nWord to guess: " + ' '.join(display))
    print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                display[index] = guess
        print(f"Good job! '{guess}' is in the word.")
    else:
        incorrect_guesses += 1
        print(f"Sorry, '{guess}' is not in the word.")

# Game result
if '_' not in display:
    print("\nCongratulations! You guessed the word:", chosen_word)
else:
    print("\nGame over! The correct word was:", chosen_word)
