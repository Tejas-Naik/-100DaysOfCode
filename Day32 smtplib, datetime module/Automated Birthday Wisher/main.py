import pandas as pd
import datetime
import random
##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
birth_data = pd.read_csv('birthdays.csv')
birth_data_month = int(birth_data.month)
birth_data_day = int(birth_data.day)

now = datetime.datetime.now()
today_month = int(now.month)
today_day = int(now.day)
# 2. Check if today matches a birthday in the birthdays.csv
if birth_data_month == today_month and birth_data_day == today_day:
    print("Dates Matched")
    temp_letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']
    letter_file = random.choice(temp_letters)
    with open(f'letter_templates/{letter_file}') as letter:
        let = letter.read()
        name_row = birth_data[birth_data.name == 'Tejas']
        let.replace('[NAME]', str(name_row.name))
        print(let)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




