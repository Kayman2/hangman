import random  #Task 2 -  Step 1: Go to the first line of your file.

#Task 1 : Create a list of words

# Step 1: Create a list containing the names of your 5 favorite fruits.
# ['banana', 'orange', 'pear', 'strawberry', 'apple']

#Step 2: Assign this list to a variable called word_list.
word_list = ['banana', 'orange', 'pear', 'strawberry', 'apple']

#Step 3: Print out the newly created list to the standard output (screen).
print("TASK 1 Step 3:    "+ str(word_list))



#TASK 2: CHOSE A RANDOM WORD FROM A LIST

#Task 2 -  Step 1: Go to the first line of your milestone2.py file.
#Task 2 -  Step 2: Write import random on the line. Note: To import a module, you have to use the import keyword at the top of the file.

# Task 2 - Step 3: Use random.choice to select a word from the list
# Task 2 - Step 4: Assign the randomly generated word to a variable called word.
word = random.choice(word_list)

#Task 2 -  Step 5: Print out word to the standard output. Run the code several times and observe the words printed out after each run.
print("TASK 2 Step 5:    "+ word)


#Task 3: ASK A USER FOR INPUT
#Task 3: Step 1: Using the input function, ask the user to enter a single letter.
#Task 3: Step 2: Assign the input to a variable called guess.
guess = input("Enter a single letter: ")

#TASK 4 : CHECK IF THE INPUT IS A SINGLE LETTER
#Task 4: Step 1: Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
#Task 4: Step 2: In the body of the if statement, print a message that says "Good guess!".
#Task 4: Step 3: Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    # Step X: Print an error message for invalid input
    print("Oops! That is not a valid input.")
