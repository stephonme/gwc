# import random

# # A list of words that 
# potential_words = ["example", "words", "someone", "can", "guess"]
guesses= ["_", "_", "_", "_", "_"]
secret_word = "pizza"
userguess= ["_"]
list= ["p", "i", "z", "z", "a"]
# Use to test your code:
# print(word)

# Converts the word to lowercase
secret_word = "pizza"
sw_len = len(secret_word)
# Make it a list of letters for someone to guess
secret_word = ["_", "_","_", "_", "_"] # TIP: the number of letters should match the word

# Some useful variables
guesses = []
maxfails = 15
fails = 0

while fails < maxfails:
	guess = input("Guess a letter: ")
    if userguess 
    
	# check if the guess is valid: Is it one letter? Have they already guessed it?

	# check if the guess is correct: Is it in the word? If so, reveal the letters!

	print(secret_word)

	fails = fails+1
	print("You have " + str(maxfails - fails) + " tries left!")