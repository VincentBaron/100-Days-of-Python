from question_model import Question
from data import question_data
from quiz_brain import QuizzDda

Question_list = []

for i in question_data:
    q_text = i["question"]
    q_answer = i["correct_answer"]
    new_question = Question(q_text, q_answer)
    Question_list.append(new_question)

quiz = QuizzDda(Question_list)

while quiz.still_has_question():
    quiz.ask_question()

print(f"You've completed the quiz!\nYour final score was : {quiz.score} / {len(quiz.question_list)}\n")