class QuizzDda:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def ask_question(self):
        answer = input(f"Q.{self.question_number + 1}: {self.question_list[self.question_number].text} "
                            f"(True/False): ")
        self.check_answer(answer)
        self.question_number += 1

    def check_answer(self, answer):
       if answer == self.question_list[self.question_number].answer.lower():
           print("You got it right mate")
           self.score += 1
       else:
           print("Wrong!")
       print(f"The correct answer was: {self.question_list[self.question_number].answer}")
       print(f"Your score is: {self.score} / {self.question_number + 1}\n")