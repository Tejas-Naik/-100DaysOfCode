from flask import Flask, render_template
import random

from flask.templating import render_template_string

random_number = random.randint(1, 10)

app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('index.html')

@app.route('/<int:guess>')
def guess(guess):
    if guess == random_number:
        return render_template('correct.html')
    elif guess < random_number:
        render_template('lower.html')
    elif guess > random_number:
        return render_template('higher.html')

if __name__ == '__main__':
    app.run(debug=True)