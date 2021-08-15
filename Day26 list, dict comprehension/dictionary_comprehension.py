import random

names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']

# the structure of a dictionary comprehsion 
# new_dict = {newkey:newvalue for (key, value) in iterable}

student_scores = {student: random.randint(1, 100) for student in names}
print(student_scores)

# scores = [58, 98, 88, 72, 94, 67, 74]
passed_students = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_students)