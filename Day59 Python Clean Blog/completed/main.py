from flask import Flask, render_template, request
import requests
import smtplib

posts = requests.get("https://api.npoint.io/0067e63917ca7a5034d9").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/form-entry', methods=['POST'])
def recieve_data():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']
    my_email = 'tejasrnaik2005@gmail.com'
    password = 'abcd1234{}'
    reciever_mail = 'rntejas2005@gmail.com'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciever_mail,
            msg=f"Subject:Quote of the Week!\n\n{message}"
        )

    return f'<h1>Successfully sent message! </h1>'

if __name__ == "__main__":
    app.run(debug=True)
