import random

class Hangman:
    """
    A class representing the Hangman game.

    Parameters:
    - word_list (list): A list of words from which the game's secret word will be chosen.
    - num_lives (int, optional): The number of lives the player has. Defaults to 5.

    Attributes:
    - word (str): The word to be guessed, randomly chosen from word_list.
    - word_guessed (list): A list representing the state of the word to be guessed, with underscores for unguessed letters.
    - num_letters (int): The number of unique letters in the word.
    - num_lives (int): The number of lives the player has.
    - word_list (list): The list of words from which the secret word is chosen.
    - list_of_guesses (list): A list of guessed letters.

    Methods:
    - check_guess(guess): Checks if the guessed letter is in the word and updates the game state.
    - ask_for_input(): Asks the player for input and manages the game loop.
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
        Check if the guessed letter is in the word and update the game state.

        Args:
        - guess (str): The letter guessed by the player.

        Returns:
        None
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
        Manage the game loop, asking the player for input and checking the validity of the guess.

        Returns:
        None
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

word_list = ['banana', 'orange', 'pear', 'strawberry', 'apple']
hangman_game = Hangman(word_list)
print("Word to guess:", hangman_game.word)
print("Word guessed so far:", hangman_game.word_guessed)
print("Number of unique letters:", hangman_game.num_letters)
print("Number of lives:", hangman_game.num_lives)
print("List of guesses:", hangman_game.list_of_guesses)

hangman_game.ask_for_input()
