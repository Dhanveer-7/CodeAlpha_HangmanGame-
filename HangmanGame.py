import random

# Predefined word list
words = ["apple", "python", "alpha", "code", "hangman"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
used_letters = []

print(" Welcome to Hangman Game!")

# Main game loop
while attempts > 0 and "_" in guessed:
    print("\nCurrent word:", " ".join(guessed))
    print("Used letters:", " ".join(used_letters))
    guess = input("Enter a letter: ").lower()

    if guess in used_letters:
        print("You already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word:
        print("Good guess!")
        for i, letter in enumerate(word):
            if letter == guess:
                guessed[i] = guess
    else:
        print("Incorrect!")
        attempts -= 1
        print("Remaining attempts:", attempts)

# Game result
if "_" not in guessed:
    print(f"\nYou won! The word was '{word}'.")
else:
    print(f"\nGame Over! The word was '{word}'.")
