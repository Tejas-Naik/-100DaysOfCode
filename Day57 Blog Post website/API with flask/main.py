from flask import Flask,redirect,url_for,render_template,request
import flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/guess/<name>')
def guess(name):
    age_responce = requests.get(f'https://api.agify.io?name={name}')
    age_data = age_responce.json()
    age = age_data['age']

    gender_responce = requests.get(f'https://api.genderize.io?name={name}')
    gender_data = gender_responce.json()
    gender = gender_data['gender']
    return render_template('guess.html', name=name.title(), gender=gender, age=age)


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)
