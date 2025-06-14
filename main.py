import random

def load_words(filename):
    with open(filename, 'r') as file:
        words = [line.strip().upper() for line in file if line.strip()]
    return words

def display_word(word, guessed_letters):
    displayed = ''.join(letter if letter in guessed_letters else '-' for letter in word)
    return displayed

def play_game():
    words = load_words('words.txt')
    secret_word = random.choice(words)
    guessed_letters = set()
    guesses_left = 8

    print("Welcome to the Word Guessing Game!")
    print("Try to guess the secret word one letter at a time.")
    print(f"The word now looks like this: {display_word(secret_word, guessed_letters)}")
    print(f"You have {guesses_left} guesses left.")

    while guesses_left > 0:
        guess = input("Type a single letter here, then press enter: ").strip().upper()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("That guess is correct.")
        else:
            print("That guess is incorrect.")
            guesses_left -= 1

        current_display = display_word(secret_word, guessed_letters)
        print(f"The word now looks like this: {current_display}")
        print(f"You have {guesses_left} guesses left.")

        if '-' not in current_display:
            print("Congratulations! You guessed the word!")
            break
    else:
        print(f"Sorry, you ran out of guesses. The word was: {secret_word}")

if __name__ == "__main__":
    play_game()
