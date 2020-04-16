"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

#from hangman_app import play_hangman
#global state
state = {'guesses':[],
		 'word':hangman_app.generate_random_word(),
		 'word_so_far': "",
		 'attempts': 6,
		 'done':False}

@app.route('/')
@app.route('/main')
def main():
	return render_template('fancymain2.html')

@app.route('/bio')
def bio():
	""" generates a bio page with links and images """
	return render_template('bio.html')

@app.route('/start')
def start():
	global state
	state['word'] = hangman_app.generate_random_word()
	state['word_so_far'] = len(state['word']) * '-'
	state['guesses'] = []
	print(state)
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])

def hangman():

	""" plays hangman game """
	global state
	if request.method == 'GET':
		return start()

	elif request.method == 'POST':
		letter = request.form['guess']
		print(state['guesses'])
		# check if letter has already been guessed
		# and generate a response to guess again

		if letter in state['guesses']:
			state['attempts'] -= 1
			state['guesses'] += [letter]
			print("That letter has been guessed, try again")
		elif not letter.isalpha():
			state['attempts'] -= 1
			state['guesses'] += [letter]
			print("That is not a letter, try again")
		elif len(letter) > 1:
			state['attempts'] -= 1
			state['guesses'] += [letter]
			print("That is more than one letter, try again")

		# else check if letter is in word

		elif letter in state['word']:
			print('Good job! That letter is in the word')
			word_so_far = hangman_app.get_word_so_far(state['word'],letter,state["guesses"])#After user guesses correct letter
			state['word_so_far'] = word_so_far						#Update word_so_far
			print(state['word_so_far'])
		elif letter not in state['word']:
			state['attempts'] -= 1
			state['guesses'] += [letter]
			print("That letter is not in the word, try again")

		# then see if the word is complete

		if state['word_so_far'] == state['word']:
			state["done"] = True
			print('Good job! You won. The word was ' +  state["word"] ) #set done to be true and tell the user they won!

		elif state['attempts'] <= 0:#the number of guesses left is zero
			state["done"] = True
			print('Sorry, you lost! The word was:'+ state["word"])#set done to be true and tell the user they lost!"

		print("attempts left: ", state['attempts'])
		#state['guesses'] += [letter]
		return render_template('play.html',state=state)



if __name__ == '__main__':
	app.run('0.0.0.0',port=3000)
