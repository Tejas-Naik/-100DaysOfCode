from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dictionary in question_data:
    question_text = dictionary['text']
    question_answer = dictionary['answer']
    new_q = Question(question_text, question_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the Quiz 👏👏")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
