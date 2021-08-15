import smtplib
import datetime
import random

with open('quotes.txt') as quotes_files:
    quotes_list = quotes_files.readlines()
    quote = random.choice(quotes_list)

my_email = 'tejasrnaik2005@gmail.com'
password = 'abcd1234{}'
reciever_mail = 'rntejas2005@gmail.com'

now = datetime.datetime.now()

with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    if True:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciever_mail,
            msg=f"Subject:Quote of the Week!\n\n{quote}"
        )
print("Sent quote!")
