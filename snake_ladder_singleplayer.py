'''
------> This game is created by shailesh paudel <-----
'''

import random
import emoji
player_pos = 0 
final_pos = 25
intstruction = """
WELCOME TO THE SNAKE 🐍🐍 AND LADDER 🪜🪜 GAME DEVELOPED BY SHAILESH PAUDEL
Instruction: 
Dice has only 4 number 1,2,3,4.
Player position is start from 0 and completed in 25. 
But between 0 to 25 there is 3 snake and 2 ladder :
Ladder:
5 -> 11
8 -> 18
Snake : 
17 -> 9
19 -> 9
24 -> 2

To complete the game you need to get exactly 25  
"""
print(intstruction)
while player_pos < final_pos :
    print("---------------------------------------------------------")
    roll = input("Enter any key to roll the dice: ")
    dice = random. randrange (1,4)
    print("Your dice number is ", dice)
    player_pos = player_pos + dice
    if player_pos == 5:
        player_pos = 11
        print("Woww!! you Climb the ladder  at 5!!")
    elif player_pos == 8:
        player_pos = 18
        print("Woww!! you Climb the ladder \U0001FA9C at 8 !!")
    elif player_pos == 24:
        player_pos = 2 
        print("Ooops!!!You are eaten by snake \U0001F40D at 24!!")
    elif player_pos == 19:
        player_pos = 7
        print("Ooops!!!You are eaten by snake \U0001F40D at 19!!")
    elif player_pos == 17:
        player_pos = 9 
        print("Ooops!!!You are eaten by snake \U0001F40D at 17!!")
    elif player_pos > final_pos:
        player_pos = player_pos - dice
        print(f"Your position is greater than 25 so Go Back at {player_pos} an retry  !!!")
    if player_pos == final_pos:
        print("Congratulations! You've won the game!")
        break
    print("Your position is ", player_pos)
print("Game Complete!")
