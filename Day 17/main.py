from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questionBank = []
for question in question_data["results"]:
    questionBank.append(Question(question["question"], question["correct_answer"])) 

quiz = QuizBrain(questionBank)

while quiz.still_has_questions():
    quiz.next_question()

print("We have reached the end of Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
