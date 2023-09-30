while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
word = "apple"  # Replace this with your actual secret word

while True:
    guess = input("Guess a letter: ")

    if len(guess) == 1 and guess.isalpha():
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
def check_guess(guess, word):
    guess = guess.lower()

    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input(word):
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, word)
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

secret_word = "apple"  
ask_for_input(secret_word)
