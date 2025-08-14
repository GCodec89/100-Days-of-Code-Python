from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

i = 0
for n in question_data:
    question_bank.append(
        Question(q_text=question_data[i]["question"], q_answer=question_data[i]["correct_answer"])
    )
    i += 1

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(
    f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_number}"
)
