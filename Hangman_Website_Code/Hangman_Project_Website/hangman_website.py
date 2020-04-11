"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route ('/mainpage')
def fancymain():
	""" renders main page """
	return render_template("fancymain2.html")

@app.route('/bio')
def bio():
	""" generates a bio page with links and images """
	return render_template('bio.html')

@app.route('/hangman_game')
def

if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
