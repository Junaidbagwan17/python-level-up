
# TODO 1: Ask the question
# todo 2: check if the answer is correct
# todo 3: Checking if were the end of the game

# Create a class called QuizBrain
class QuizBrain:
    #write init() method
    def __init__(self, q_list):
        self.q_number = 0 # initalize question number to default 0
        self.score = 0
        self.question_list = q_list # initailize the quesionlist input(question bank list)


# create method calld still have questions and return a boolean based on value of q_number
    def still_have_question(self):
        return self.q_number < len(self.question_list)

# retrive the item from the current question number from the quesiton list,
    # use the input() to to show the user question text and ask for the users answer
    def next_question(self):
        current_question = self.question_list[self.q_number]
        self.q_number += 1
        user_answer = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("that's wrong.")
        print("the answer was: " + user_answer)
        print(f"Your current score is {self.score}/{self.q_number}")
        print("\n")
