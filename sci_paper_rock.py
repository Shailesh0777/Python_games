import random

user = input("Enter your choice (Scissor, Paper and Rock):")
computer = random.choice(["Scissor","Paper","Rock"])
print("Computer choice is: ",computer)
if user == computer:
    print("Its a Draw")
elif  (user == "Scissor" and computer == "Paper") or (user == "Paper" and computer == "Rock" ) or (user == "Rock" and computer == "Scissor" ):
    print("You win computer lose")
else:
    print("Computer win you lose")
      

