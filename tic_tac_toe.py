import emoji
instruction = """ 
This wiil be our Tic Tac Toe Board
 1 | 2 | 3
---|---|---
 4 | 5 | 6  
---|---|---
 7 | 8 | 9



 instruction = 
 1. Enter (1-9) to draw your sign in that respective place
 2. After filling all spots result will publish
 3. Player one goes first
 """

heart_emoji = emoji.emojize(":red_heart:")

sign_dict = []
for i in range(9):
    sign_dict.append(' ')

def print_board():
    board = f"""
     {sign_dict[0]} | {sign_dict[1]} | {sign_dict[2]}
    ---|---|---
     {sign_dict[3]} | {sign_dict[4]} | {sign_dict[5]}  
    ---|---|---
     {sign_dict[6]} | {sign_dict[7]} | {sign_dict[8]}

"""
    print(board)

# if user enter greater than 9
index_list = []
def take_input(player_name):
  while True:
    x = int(input(f'{player_name}: '))
    x -= 1
    if 0 <= x < 10:
      if x in index_list:
        print('This spot is blocked.')
        continue
      index_list.append(x)  
      return x
    print('Please Enter number between 1-9')

#result calultinh
def calculate_result(sign_dict, player_one, player_two):
  if sign_dict[0] == sign_dict[1] == sign_dict[2] == 'X'or \
    sign_dict[1] == sign_dict[4] == sign_dict[7] == 'X' or \
    sign_dict[0] == sign_dict[4] == sign_dict[8] == 'X' or \
    sign_dict[2] == sign_dict[5] == sign_dict[8] == 'X' or \
    sign_dict[3] == sign_dict[4] == sign_dict[5] == 'X' or \
    sign_dict[2] == sign_dict[4] == sign_dict[6] == 'X' or \
    sign_dict[6] == sign_dict[7] == sign_dict[8] == 'X' or \
    sign_dict[0] == sign_dict[3] == sign_dict[6] == 'X' :
    print(f'Congratulations {player_one}. You WON.!!')
    quit(f'Thank you both for joining {heart_emoji} {heart_emoji}')
  elif sign_dict[0] == sign_dict[1] == sign_dict[2] == 'O' or \
       sign_dict[1] == sign_dict[4] == sign_dict[7] == 'O' or \
       sign_dict[0] == sign_dict[4] == sign_dict[8] == 'O' or \
       sign_dict[2] == sign_dict[5] == sign_dict[8] == 'O' or \
       sign_dict[3] == sign_dict[4] == sign_dict[5] == 'O' or \
       sign_dict[2] == sign_dict[4] == sign_dict[6] == 'O' or \
       sign_dict[6] == sign_dict[7] == sign_dict[8] == 'O' or \
       sign_dict[0] == sign_dict[3] == sign_dict[6] == 'O' :
    print(f'Congratulations {player_two}. You WON.!!')
    quit(f'Thank you both for joining {heart_emoji} {heart_emoji}')
  else:
    return


def main():
    print(f"WELCOME TO THE GAME!! {heart_emoji} {heart_emoji} ")
    player_one = input("Enter the name of player one :")
    player_two = input("Enter the name of player two :") 
    print(f"Thank you {player_one} and {player_two} for joining in our game {heart_emoji} {heart_emoji} !!!")

    print(instruction)

    print(f"{player_one}'s sign will be - X")
    print(f"{player_two}'s sign will be - O")

    input("\nEnter any key to start the game: ")

    print_board()
    for i in range(9):
        if i % 2 == 0:
            index = take_input(f"Its {player_one} turn")
            sign_dict[index] = 'X'
        else:
            index = take_input(f"Its {player_two} turn")
            sign_dict[index] = 'O'
        print_board()
        calculate_result(sign_dict, player_one, player_two)
    print("This is a tie..!! Nobody won. Play Again.")

main()