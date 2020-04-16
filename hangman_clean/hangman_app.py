"""
   hangman_app.py is an app for playing hangman in the terminal
   it is also used as a module in the hangman_webapp flask app
"""
import random
def generate_random_word():
	filename = "words.txt"
	file = open(filename,"r")  # the "r" specifies we will be reading from it, not writing to it
	text = file.read()
	words = text.split()
	return random.choice(words)
#generate_random_word()

word = str(generate_random_word())
guesses = []


def get_word_so_far(word,n,guesses):
	w = len(word)
	guesses += n
	wordTest = word
	for i in word:
		if i not in guesses:
			wordTest = wordTest.replace(i,'-',w)
	return wordTest
#get_word_so_far(word)

def guessed_letters_str(guessed_letters):
	# initialize an empty string \n",
	str_guessed_letters = ''
   # return string   \n",
	return (str_guessed_letters.join(guessed_letters))
#guessed_letters_str(guessed_letters)
