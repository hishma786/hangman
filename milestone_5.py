import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))  
        self.list_of_guesses = []

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
game = Hangman(word_list)
print(f"Word to guess: {' '.join(game.word_guessed)}")
print(f"Number of lives: {game.num_lives}")
print(f"Number of unique letters in the word: {game.num_letters}")
print(f"List of guesses: {game.list_of_guesses}")
import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(guess)  
                self.list_of_guesses.append(guess)  

word_list = ["apple", "banana", "cherry", "date", "elderberry"]
game = Hangman(word_list)
game.ask_for_input()  

class Hangman:

    def check_guess(self, guess):
        guess = guess.lower()  
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
        else:
            self.num_lives -= 1  
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
def play_game(word_list):
    num_lives = 5  
    game = Hangman(word_list, num_lives)  

    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

play_game(word_list)

      
