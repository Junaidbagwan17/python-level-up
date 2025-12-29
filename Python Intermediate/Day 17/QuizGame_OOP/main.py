# import classs model and data
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#TODO 1: write a for loop to iterate over the question_data
# create a Question object from each entry in question_Data
# append each question object to the question bank
question_bank = []

for i in question_data:
    text = i["text"]
    answer = i["answer"]
    # To combine text + answer into one object
    new_question = Question(text, answer)
    question_bank.append(new_question)
print(question_bank)

quiz = QuizBrain(question_bank)
while quiz.still_have_question(): # if quiz still has questions
    quiz.next_question()

print(f"You have completed the quiz")
print(f"Your final score was: {quiz.score} / {quiz.q_number}")