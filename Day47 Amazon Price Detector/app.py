import requests
from unidecode import unidecode
import smtplib
from bs4 import BeautifulSoup
import lxml

my_email = 'tejasrnaik2005@gmail.com'
password = 'abcd1234{}'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0Win64x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Safari/537.36",
    'Accept-Language': "en-US, en;q = 0.9"
}

url = 'https://www.amazon.in/Apple-MLA22HN-Magic-Keyboard-White/dp/B01AWB04GG/ref=sr_1_2_sspa?dchild=1&keywords=apple+magic+keyboard&qid=1614923486&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyT1JFQUdPQUhBNTg0JmVuY3J5cHRlZElkPUEwMDkwMTkzVFUxT04yWDJQMUgwJmVuY3J5cHRlZEFkSWQ9QTAwNDg1NzMyUkI0MTZEU1FRQUNMJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==' 

amazon_response = requests.get(
    url, headers=headers)
amazom_html = amazon_response.content

soup = BeautifulSoup(amazom_html, 'lxml')
price = soup.find(id='priceblock_ourprice').get_text().split('₹')[1]
price = unidecode(price).split(',')
price = price[0]+price[1]
price = float(price)

product_name = soup.find(id='productTitle').get_text().strip()

lowest_price = int(input(f"the current price of {product_name} is {price} Please enter the lowest price you can pay for this: "))
if price < lowest_price:
    reciever_mail = 'rntejas2005@gmail.com'  # 'wrajendranaik1771@gmail.com'
    # we must provide port number as 587 on windows
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()  # tls = transport layer security (securing our connection)
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciever_mail,
            msg=f"Subject:{product_name} is on SALE\n\nHello, \nThe Price of the {product_name} is below your expectations!! \nPlease go and checkout\n{url}"
        )
    print("Sent the Mail")
else:
    print("Sorry! the product price is higher than your expectations!!")
