import pandas
student_scores = {
    'student': ['tejas', 'angela', 'james', 'williams'],
    'scores': [69, 98, 76, 83]
}

# looping through the dictionaries
for (key, value) in student_scores.items():
    print(key, value)

df = pandas.DataFrame(student_scores)
print(df)

# Looping through a data frame
# Looping through a data frame by rows
for (index, row) in df.iterrows():
    if row.student == 'tejas':
        print(index, row)
