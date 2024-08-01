'''
------> This game is created by shailesh paudel <-----
      -----> This game will run in terminal <-------
'''


import random
import time

instruction = '''
WELCOME TO THE TIMED MATH CHALLENGE GAME DEVELOPED BY SHAILESH PAUDEL💕💕

instruction =
Number are between 3 to 12 so this is not so hard and the operations are only
addition, subtraction and multiplicaton.
Computer randomly generate the number and operator and 
you should answer the question fast as you can 
if your answer is correct then you will be able to solve another problem 
otherwise the same problem will repeated until you give the right answer 
And you can solve the n number of problem and the computer computed the time you take 
to solve n number of problem...
This game help you to boost your knowledge in mathematics
'''

print(instruction)
OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = int(input("Enter the number of problems: "))

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expression = str(left) + " " + operator + " " + str(right)
    result = eval(expression)
    return expression, result

wrong = 0
input("Press Enter to Start!")
print("--------------------")

start_time = time.time()
for i in range (TOTAL_PROBLEMS):
    expression, result = generate_problem()
    while True:
        guess = input("Problem Number " +str (i + 1) + " : " + expression + " = ")
        if guess == str(result): 
            break 
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("---------------------")
print(f"Good Job! You finished the challenge in {total_time} seconds!!")