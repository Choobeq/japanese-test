# Test to practice Japanese Vocabulary for Black Belt Exam.
# qn = question number
# ua = user answer

# Importing libraries
import random, os
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

# Main loop to ask 10 questions
while counting_steps < 10:
    qn = random.randint(0,95)
    if questions[qn] in temp_questions: # Checking if the question was already in this run.
        continue
    else:
        counting_steps += 1
        temp_questions.append(questions[qn])
        print(f"\nQuestion number {counting_steps}\t: {questions[qn]}")
        ua = input('Your answer here\t: ').upper()
        
        # Checking each word separately to identify if words are correct but in different order
        diff_set = set(answers[qn].split()).symmetric_difference(set(ua.split()))
        if ua == answers[qn]:
            print('Correct!')
            counting_correct_answers += 1
        elif len(diff_set) == 0:
            print('Correct words but different order!')
            print(f'Order in database\t: {answers[qn]}')
            counting_correct_answers += 1
        else: 
            print('Incorrect!')
            print(f"Correct answer is\t: {answers[qn]}")

# Printing message on the screen with the score.
print(f'You Have Scored {counting_correct_answers} Points!')

# Checking if the score is single digit and converting it to double digits if needed.
if len(str(counting_correct_answers)) < 2:
    digits = "0"+str(counting_correct_answers)    
else:
    digits = counting_correct_answers

# Checking if the file 'statistics.csv' exists,
# and creates one if it doesn't. 
if not os.path.exists('statistics.csv'):
    with open('statistics.csv', "w", encoding="utf-8") as statistics:
        statistics.write("┌────────────┬───────┬───────┐\n")
        statistics.write("│    DATE    │ TIME  │ SCORE │\n")
        statistics.write("├────────────┼───────┼───────┤\n")

# Saving current score to the file "statistics.csv"
with open('statistics.csv', 'a', encoding="utf-8") as f3:
    current_time = datetime.now().strftime("%H:%M")
    f3.write(f"│ {today} │ {current_time} │   {digits}  │\n")
    f3.write(f"├────────────┼───────┼───────┤\n")
