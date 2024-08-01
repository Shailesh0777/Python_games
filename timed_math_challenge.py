import random
import time
OPERATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10    

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