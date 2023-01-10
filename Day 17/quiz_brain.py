class QuizBrain:
    def __init__(self, inputlist):
        self.question_number = 0
        self.question_list = inputlist
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        questionNow = self.question_list[self.question_number]
        self.question_number += 1
        userAnswer = input(f"\nQ {self.question_number}. {questionNow.question} (True/False)?")
        self.check_answer(userAnswer, questionNow.answer)
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That was wrong.")
        
        print(f"The correct answer is {correct_answer}")
