'''
------> This game is created by shailesh paudel <-----
'''
import random

instruction = '''
WELCOME TO THE SCISSOR✂️ , PAPER📄 AND ROCK🪨 GAME
 
instruction = 
make your choice by typing Scissor or Paper or Rock 
then computer will choose its choice and compute the result
'''
print(instruction)
user = input("Enter your choice (Scissor, Paper and Rock):")
computer = random.choice(["Scissor","Paper","Rock"])
print("Computer choice is: ",computer)
if user == computer:
    print("Its a Draw")
elif  (user == "Scissor" and computer == "Paper") or (user == "Paper" and computer == "Rock" ) or (user == "Rock" and computer == "Scissor" ):
    print("You Won!!")
else:
    print("You lose!!")
      

