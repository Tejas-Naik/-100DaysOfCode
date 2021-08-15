import smtplib  # the SMTP lib is a great library to sending Emails using Python

# to create an SMTP object we use smtplib.SMTP
"""
    if you have different email service provider like yahoo use the following code
    GMAIL = smtp.gmail.com
    HOTMAIL = smtp.live.com
    YAHOO = smtp.mail.yahoo.com
"""
# gmail = tejasrnaik2005@gmail.com
# pass_gmail = abcd1234{}
# yahoo = tejasnaik2005@yahoo.com
# pass_yahoo = abcd1234{}
# yahoo app password = 'wjgshzbbpowfnxce'

my_email = 'pythonbot2005@gmail.com'
password = 'pythonbot'
reciever_mail = 'wrajendranaik1771@gmail.com'  # 'wrajendranaik1771@gmail.com'
with smtplib.SMTP('smtp.gmail.com', 587) as connection:     # we must provide port number as 587 on windows
    connection.starttls()  # tls = transport layer security (securing our connection)
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=reciever_mail,
        msg="Subject:Python automated mail\n\nHello, This is the mail sent using Python like if you get it!!"
    )
# pythonbot2005@gmail.com
# pythonbot