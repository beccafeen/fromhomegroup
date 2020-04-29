import random
def generate_random_word():
		filename = "words.txt"
		file = open(filename,"r")  # the "r" specifies we will be reading from it, not writing to it
		text = file.read()
		words = text.split()
		return random.choice(words)
generate_random_word()

word = str(generate_random_word())
guessed_letters = []

def guessed_letters_str(guessed_letters):
		# initialize an empty string \n",
		str_guessed_letters = ''
	 # return string   \n",
		return (str_guessed_letters.join(guessed_letters))
guessed_letters_str(guessed_letters)

def play_hangman():
		HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /   \
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /   \
|   |
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /   \
|   |
|  |
|
|
--------
""",
"""
-----
|   |
|   0
| /   \
|   |
|  | |
|
--------
""")
		want_to_play = True
		play = input('Do you want to play hangman?'.lower())

		if play not in ("yes","y"):
				want_to_play = False
				print('Goodbye')



		while want_to_play == True:
				guessed_letters = []
				word = str(generate_random_word())
				print(HANGMAN[0])
				letter = input('Please choose a letter') #"ask the user for a letter"
				attempts = (len(HANGMAN) - 1)

				def print_word():
						w = len(word)
						wordTest = word
						for i in word:
								if i not in guessed_letters:
										wordTest = wordTest.replace(i,'-',w)
						print(wordTest)
						if wordTest == word:
								want_to_play = False

				print_word()

				done = False
				while not done:

						while (attempts != 0 and set(word) != set(guessed_letters_str(guessed_letters))):



								if not letter.isalpha(): # check the input is a letter. Also checks an input has been made.
										attempts -= 1
										print(HANGMAN[(len(HANGMAN) - 1) - attempts])
										print("That is not a letter.")
										print(("\nYou have {} attempts remaining\n").format(attempts))

								elif len(letter) > 1: # check the input is only one letter
										attempts -= 1
										print(HANGMAN[(len(HANGMAN) - 1) - attempts])
										print("That is more than one letter.")
										print(("\nYou have {} attempts remaining\n").format(attempts))

								elif letter in guessed_letters:
										attempts -= 1
										print(HANGMAN[(len(HANGMAN) - 1) - attempts]) #subtract one from guesses_left
										print('You have already guessed that letter') #and tell them they already guessed that letter
										print(("\nYou have {} attempts remaining\n").format(attempts))

								elif letter not in word:
										attempts -= 1
										print(HANGMAN[(len(HANGMAN) - 1) - attempts])
										guessed_letters.append(letter) #add letter to guessed letters
										print('That letter is not in this word')#tell user the letter is not in the word
										print("\nLetters guessed:",guessed_letters)#prints list of guessed letters
										print(("\nYou have {} attempts remaining\n").format(attempts))

								elif letter in word:
										print(HANGMAN[(len(HANGMAN) - 1) - attempts])
										guessed_letters.append(letter) #add letter to guessed letters
										print('Good job! That letter is in the word') #tell user the letter is in the word
										print("\nLetters guessed:",guessed_letters)#prints list of guessed letters
										print(("\nYou have {} attempts remaining\n").format(attempts))

								if set(word) <= set(guessed_letters_str(guessed_letters)):
										print(HANGMAN[(len(HANGMAN) - 1) - attempts])
										done = True
										print('Good job! You won. The word was ' +  word ) #set done to be true and tell the user they won!
										break

								elif attempts <= 0:#the number of guesses left is zero
										done = True
										print('Sorry, you lost, the word was ' +  word)#set done to be true and tell the user they lost!"
										break

								else:
										print_word()#print the word with a dash for each letter not in guessed_letters
										letter = input('\nPlease choose another letter') #ask the user for another letter"

				print("Would you like to play again?")

				response = input("> ").lower()
				if response not in ("yes","y"):
						want_to_play = False
						print('Goodbye')
						return

#if __name__ == "__main__":
		#play_hangman()
