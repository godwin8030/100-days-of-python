from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for items in question_data:
    question_text = items["text"]
    question_ans = items["answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.continue_questions:
    quiz.next_question()

print("Hurray! You have completed the quiz")
print(f"The final score is: {quiz.score}/{len(question_bank)}")