"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
import hangman_app
app = Flask(__name__)

from hangman_app import play_hangman
#global state
state = {'guesses':[],
         'word':hangman_app.generate_random_word(),
         #'word_so_far': 'pie',
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
	state['guesses'] = []
	return render_template("start.html",state=state)

@app.route('/play',methods=['GET','POST'])
def hangman():
	""" plays hangman game """
	global state
	if request.method == 'GET':
		return play()

	elif request.method == 'POST':
		letter = request.form['guess']
		# check if letter has already been guessed
		# and generate a response to guess again
		# else check if letter is in word
		# then see if the word is complete
		# if letter not in word, then tell them
		state['guesses'] += [letter]
		return render_template('play.html',state=state)



if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
