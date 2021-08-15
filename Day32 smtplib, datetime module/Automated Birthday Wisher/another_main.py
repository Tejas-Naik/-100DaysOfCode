from datetime import datetime
import pandas
import random
import smtplib

today_tuple = (datetime.now().month, datetime.now().day)

data = pandas.read_csv('birthdays.csv')

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    print(birthday_person)
    file_path = f'letter_templates/letter_{random.randint(1,3)}.txt'
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', str(birthday_person['Name']))
        print(contents)

    my_email = 'tejasrnaik2005@gmail.com'
    password = 'abcd1234{}'

    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday\n\n{contents}"
        )
