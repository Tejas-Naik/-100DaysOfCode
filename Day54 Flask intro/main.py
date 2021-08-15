import random
from flask import Flask, render_template

app = Flask(__name__)

random_number = random.randint(1, 11)
def make_bold(func):
   def wrapper():
      return '<b>' + func() + '</b>'
   return wrapper

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/bye')
@make_bold
def bye():
   return "Bye"

@app.route('/<number>')
def greet(number):
   if int(number) < random_number:
      return render_template('higher.html')
   elif int(number) > random_number:
      return render_template('lower.html')
   else:
      return render_template('correct.html')



if __name__ == '__main__':
    app.run(debug=True)
