from flask import Flask, redirect, url_for, render_template, request
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    year = datetime.now().year
    random_number = randint(0, 10)
    return render_template('index.html', number=random_number, year=year)


@app.route('/blog')
def blog():
    blog_url = "https://www.npoint.io/docs/ed99320662742443cc5b"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template('blog.html', posts=all_posts)


if __name__ == '__main__':
    # DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000, debug=True)
