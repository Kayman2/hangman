import random



# Create a list of words assigned to a variable called word_list
word_list = ['banana', 'orange', 'pear', 'strawberry', 'apple']

# Chose a random word from the list
word = random.choice(word_list)

#print("TASK1 WORD==========  "+ word)

# Create a while loop that runs continuously
while True:
    # Ask the user to guess a letter and assign it to a variable called guess
    guess = input("Guess a letter: ")

    # Check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        # Step 4: If the guess is valid, break out of the loop
        break
    else:
        # If the guess is invalid, print an error message
        print("Invalid letter. Please, enter a single alphabetical character.")



# TASK 2:

# Choose a random word from the list
word = random.choice(word_list)

#print("TASK2 WORD==========  "+ word)

# Create a while loop that runs continuously
while True:
    # Ask the user to guess a letter and assign it to a variable called guess
    guess = input("Guess a letter: ")

    # Check if the guess is a single alphabetical character
    if guess.isalpha() and len(guess) == 1:
        # If the guess is valid, check if it's in the word
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
            #break
        else:
            print(f"Sorry, {guess} is not in the word. Try again.")
    else:
        # If the guess is invalid, print an error message
        print("Invalid letter. Please, enter a single alphabetical character.")


# TASK 3:
# Choose a random word from the list
word = random.choice(word_list)

#print("TASK3 WORD==========  "+ word)

def check_guess(guess):
    """
    Check if the guessed letter is in the randomly selected word.

    Args:
        guess (str): The letter guessed by the user.

    Returns:
        None
    """
    # Convert the guess into lower case
    guess = guess.lower()

    # Check if the guess is in the word
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
    """
    Continuously ask the user to guess a letter and check its validity.

    Args:
        None

    Returns:
        None
    """
    while True:
        # Ask the user to guess a letter and assign it to a variable called guess
        guess = input("Guess a letter: ")

        # Check if the guess is a single alphabetical character
        if guess.isalpha() and len(guess) == 1:
            break
        else:
            # If the guess is invalid, print an error message
            print("Invalid letter. Please, enter a single alphabetical character.")

    # Call the check_guess function to check if the guess is in the word
    check_guess(guess)

# Call the ask_for_input function to test the code
ask_for_input()

