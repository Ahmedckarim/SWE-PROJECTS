# list of questions 
# store the answers
# randomly pick question
# ask the user
# see if they correct 
# keep track of the score 
# tell the user thier score 

import random

questions = {
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
    questions_list = list(questions.keys())
    total_questions = 5
    score = 0

    select_questions = random.sample(questions_list, total_questions)

    for i,question in enumerate(select_questions, start= 1):
        print(f"{i}. {question}")
        user_answer = input("Your answer: ").lower().strip()

        correct_answer = questions[question].lower()

        if correct_answer == user_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. the correct answer is {correct_answer}")
    print(f"Game over! your final score is {score}\{total_questions}")

    
    

trivia_game()