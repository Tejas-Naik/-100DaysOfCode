import smtplib
from flask import Flask, request
from flask.templating import render_template
import requests

app = Flask(__name__)

blog_url = "https://api.npoint.io/0067e63917ca7a5034d9"
blog_data = requests.get(blog_url)
all_posts = blog_data.json()


@app.route('/')
def home_page():
    return render_template("index.html", posts=all_posts)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<id>')   # The id is coming from index.html
def post_page(id):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == int(id):
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/send-mail", methods=['post'])
def send_mail():
    name = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    
    my_email = 'tejasrnaik2005@gmail.com'
    password = 'abcd1234{}'
    reciever_mail = 'rntejas2005@gmail.com'
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        if True:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=reciever_mail,
                msg=f"Subject:Your Customer's review on your blog site1\n\n{name}\n{email}\n{phone}\n{message}"
            )

    return f"<h1>{name}, your Message sent successfully!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
