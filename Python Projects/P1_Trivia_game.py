# list of questions 
# store the answers
# randomly pick question
# ask the user
# see if they correct 
# keep track of the score 
# tell the user thier score 

import random

Questions = {
    "What does CPU stand for?": "Central Processing Unit",
    "What does RAM stand for?": "Random Access Memory",
    "What does HTML stand for?": "HyperText Markup Language",
    "What does CSS stand for?": "Cascading Style Sheets",
    "What does HTTP stand for?": "HyperText Transfer Protocol",
    "What is the brain of the computer?": "CPU",
    "What does OS stand for?": "Operating System",
    "What does URL stand for?": "Uniform Resource Locator",
    "Which data structure stores key-value pairs?": "Dictionary",
    "What programming language is widely used for AI and machine learning?": "Python"
}

def trivia_game():
    print("Wlecome to Quiz game")
    Questions_list = list(Questions.keys())
    total_questions = 5
    score = 0

    select_questions = random.sample(Questions_list, total_questions)

    for i,question in enumerate(select_questions, start= 1):
        print(f"{i}. {question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = Questions[question]

        if correct_answer.lower() == user_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. the correct answer is {correct_answer}")
    print(f"Game over! your final score is {total_questions}/{score}\n")

    
    

trivia_game()