# This is a test to practice Japanese Vocabulary for black belt exam.
# qn = question number
# ua = user answer

import random
from datetime import date, datetime

# Declaring variables
today = date.today()
questions = []
answers = []
counting_correct_answers = 0
temp_questions = []
diff_set = ()
counting_steps = 0

# Reading vocabulary in English from the file "questions.csv"
with open('questions.csv') as f1:
    questions = f1.read().splitlines()

# Reading vocabulary in Japanese from the file "answers.csv"
with open('answers.csv') as f2:
    answers = f2.read().splitlines()

#for z in range(0,10):
while counting_steps < 10:
    qn = random.randint(0,95)
    if questions[qn] in temp_questions:
        continue
    else:
        counting_steps += 1
        temp_questions.append(questions[qn])
        print(f"\nQuestion number {counting_steps}\t: {questions[qn]}")
        ua = input('Your answer here\t: ').upper()
        diff_set = set(answers[qn].split()).symmetric_difference(set(ua.split()))
        if ua == answers[qn]:
            print('Correct!')
            counting_correct_answers += 1
        elif len(diff_set) == 0:
            #print(diff_set)
            print('Correct words but different order!')
            print(f'Order in database\t: {answers[qn]}')
            counting_correct_answers += 1
        else: 
            print('Incorrect!')
            print(f"Correct answer is\t: {answers[qn]}")

# Printing message on the screen with the score.
print(f'You Have Scored {counting_correct_answers} Points!')

# Checking if the score is single digit and converting to double digit if needed.
if len(str(counting_correct_answers)) < 2:
    digits = "0"+str(counting_correct_answers)    
else:
    digits = counting_correct_answers

current_time = datetime.now().strftime("%H:%M")

# Saving current score to the file "statistics.csv"
with open('statistics.csv', 'a') as f3:
    current_time = datetime.now().strftime("%H:%M")
    f3.write(F"| {today} | {current_time} |   {digits}  |\n")
    f3.write(F"|------------|-------|-------|\n")
