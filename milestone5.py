import random


class Hangman:
    """
    A class representing the Hangman game.

    ... (rest of the class docstring) ...
    """

    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(self, guess):
        """
        ... (check_guess docstring) ...
        """

        guess = guess.lower()

        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            updated_word_guessed = []
            for letter, guessed_letter in zip(self.word, self.word_guessed):
                if letter == guess:
                    updated_word_guessed.append(letter)
                else:
                    updated_word_guessed.append(guessed_letter)

            self.word_guessed = updated_word_guessed
            self.num_letters -= self.word.count(guess)
        else:
            if guess in self.list_of_guesses:
                print(f"You already tried that letter!")
            else:
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left.")
                self.list_of_guesses.append(guess)

    def ask_for_input(self):
        """
        ... (ask_for_input docstring) ...
        """
        while self.num_letters > 0 and self.num_lives > 0:
            guess = input("Guess a letter: ")

            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            else:
                self.check_guess(guess)

            if self.num_letters == 0:
                print("Congratulations! You guessed the word.")
                break
            elif self.num_lives == 0:
                print("Out of lives! The word was:", self.word)
                break
            elif all(letter != '_' for letter in self.word_guessed):
                print("Congratulations! You guessed the word.")
                break


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


word_list = ['banana', 'orange', 'pear', 'strawberry', 'apple']
play_game(word_list)
