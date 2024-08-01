import random
import emoji
player1_pos = 0 
player2_pos = 0
final_pos = 25
player1 = input("Enter the name of player1: ")
player2 = input("Enter the name of player2: ")

while player1_pos < final_pos :
    #Player 1 turn    
    print("--------------------------------------------------------------------------------------------------")
    roll = input(f"{player1} turn to roll the dice : ")
    dice = random. randrange (1,4)
    print(f"{player1} dice number is ", dice)
    player1_pos = player1_pos + dice
    if player1_pos == 5:
        player1_pos = 11
        print(f"Woww!! {player1} Climb the ladder \U0001FA9C  at 5!!")
    elif player1_pos == 8:
        player1_pos = 18
        print(f"Woww!! {player1} Climb the ladder \U0001FA9C at 8 !!")
    elif player1_pos == 24:
        player1_pos = 2 
        print(f"Ooops!!!{player1} is eaten by snake \U0001F40D at 24!!")
    elif player1_pos == 19:
        player1_pos = 7
        print(f"Ooops!!!{player1} is eaten by snake \U0001F40D at 19!!")
    elif player1_pos == 17:
        player1_pos = 9 
        print(f"Ooops!!!{player1} is eaten by snake \U0001F40D at 17!!")
    elif player1_pos == player2_pos:
        player2 = 0
        print(f"{player2} is sent back to 0 by {player1}")
    elif player1_pos > final_pos:
        player1_pos = player1_pos - dice
        print(f"{player1} position is greater than 25 so Go Back at {player1_pos} an retry  !!!")
    if player1_pos == final_pos:
        print(f"Congratulations! {player1} won the game!")
        break
    print(f"{player1} position is ", player1_pos)

#--------------------------------------------------------------------------------------------------------
# Player 2 turn 
    print("--------------------------------------------------------------------------------------------------")
    roll = input(f"{player2} turn to roll the dice : ")
    dice = random. randrange (1,4)
    print(f"{player2} dice number is ", dice)
    player2_pos = player2_pos + dice
    if player2_pos == 5:
        player2_pos = 11
        print(f"Woww!! {player2} Climb the ladder \U0001FA9C  at 5!!")
    elif player2_pos == 8:
        player2_pos = 18
        print(f"Woww!! {player2} Climb the ladder \U0001FA9C at 8 !!")
    elif player2_pos == 24:
        player2_pos = 2 
        print(f"Ooops!!!{player2} is eaten by snake \U0001F40D at 24!!")
    elif player2_pos == 19:
        player2_pos = 7
        print(f"Ooops!!!{player2} is eaten by snake \U0001F40D at 19!!")
    elif player2_pos == 17:
        player2_pos = 9 
        print(f"Ooops!!!{player2} is eaten by snake \U0001F40D at 17!!")
    elif player2_pos == player1_pos:
        player1_pos = 0
        print(f"{player1} is sent back to 0 by {player2}")
    elif player2_pos > final_pos:
        player2_pos = player2_pos - dice
        print(f"{player2}r position is greater than 25 so Go Back at {player2_pos} an retry  !!!") 
    if player2_pos == final_pos:
        print(f"Congratulations! {player2} won the game!")
        break
    print(f"{player2} position is ", player2_pos)