from random import choice as random_choice

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word = random_choice(word_list)
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set([chara for chara in self.word]))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for index in range(len(self.word)):
                if self.word[index] == guess:
                    self.word_guessed[index] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.\nYou have {self.num_lives} " + "lives left." if self.num_lives > 1 else "life left.")

    def ask_for_input(self):
        while True:
            guess = input("Guess a letter: ")
            guess = guess.lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You have already tried that letter!")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    print(game.word)
    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game.num_letters > 0:
            print(''.join(map(str, game.word_guessed)))
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break

with open("words.txt", "r") as words:
    play_game(words.read().split())