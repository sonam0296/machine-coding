import random
import sys

BOARD_SIZE = 100
DICE = 6

snakes = {
    17: 7,
    54: 34,
    63: 18,
    64: 60,
    87: 36,
    92: 73,
    95: 75,
    98: 79
}

ladder = {
    4: 14,
    9: 31,
    21: 42,
    28: 84,
    51: 68,
    72: 91,
    80: 99
}

player_turn_text = [
    'Your turn..',
    'Goo..',
    'Lets win this game',
    'Are you ready? '
    ''
]

snake_bite = [
    "boohoo",
    "bummer",
    "snake bite",
    "oh no",
    "dang"
]
ladder_jump = [
    "woohoo",
    "woww",
    "nailed it",
    "oh my God...",
    "yaayyy"
]

def welcome_message():
    msg= """
    Welcome to Snake and Ladder Game.
    Version: 1.0.0
    Developed by: Sonam Jha
Rules:
      1. Initally both the players are at starting position i.e. 0. 
         Take it in turns to roll the dice. 
         Move forward the number of spaces shown on the dice.
      2. If you lands at the bottom of a ladder, you can move up to the top of the ladder.
      3. If you lands on the head of a snake, you must slide down to the bottom of the snake.
      4. The first player to get to the FINAL position is the winner.
      5. Hit enter to roll the dice.
"""
    print(msg)

def get_player_name():
    player_name1 = None
    while not player_name1:
        player_name1 = input("Please enter your good name for first player!!!").strip()
    
    player_name2 = None
    while not player_name2:
        player_name2 = input("Please enter your good name for second player!!!").strip()
    
    print(f'Match will be played between {player_name1} & {player_name2}')
    return player_name1, player_name2


def get_dice_values():
    dice_value = random.randint(1, DICE)  
    print(f'Its a {dice_value}')
    return dice_value  

def got_snake_bite(old_value, curr_value, player_name):
    print( "\n" + random.choice(snake_bite).upper() + " ------>>>>")
    print(f'{player_name} got a snake bite. Go down from {str(old_value)} to {str(curr_value)}')
    
def got_ladder_jump(old_val, curr_val, player_name):
    print("\n" + random.choice(ladder_jump).upper() + " ------>>>>")
    print(f'{player_name} got a jump. Go up from {str(old_val)} to {str(curr_val)}')
    
def snake_ladder(player, curr_val, dice_val):
    print( ':::::DICE_VALUE:::::', curr_val)
    old_value = curr_val
    curr_val = curr_val + dice_val
    
    if curr_val > BOARD_SIZE:
        print(f'You need {str(BOARD_SIZE - old_value)} to win this game!! Keep trying.... ')
        return old_value
    
    print("\n" + player + " moved from " + str(old_value) + " to " + str(curr_val))
    if curr_val in snakes:
        final_value = snakes.get(curr_val)
        got_snake_bite(curr_val, final_value, player)
    elif curr_val in ladder:
        final_value = ladder.get(curr_val)
        got_ladder_jump(curr_val, final_value, player)
    else: 
        final_value = curr_val
    
    return final_value

def check_win(player_name, position):
    if BOARD_SIZE == position:
        print("\n\n\nThats it.\n\n" + player_name + " won the game.")
        print("Congratulations " + player_name)
        print("\nThank you for playing the game. Hope you enjoyed the time with your friend Sonam\n\n")
        sys.exit(1)

def start_game():
    welcome_message()
    player_name1, player_name2 = get_player_name()
    
    player1_current_position = 0
    player2_current_position = 0
    
    while True:
        input_1 = input("\n" + player_name1 + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_values()
        print(player_name1 + " moving....")
        print(player1_current_position, ":::::::::132line::::::")
        player1_current_position = snake_ladder(player_name1, player1_current_position, dice_value)
        check_win(player_name1, player1_current_position)
        
        input_2 = input("\n" + player_name2 + ": " + random.choice(player_turn_text) + " Hit the enter to roll dice: ")
        print("\nRolling dice...")
        dice_value = get_dice_values()
        print(player2_current_position, ":::::::::139line::::::")
        print(player_name2 + " moving....")
        player2_current_position = snake_ladder(player_name2, player2_current_position, dice_value)
        check_win(player_name2, player2_current_position)
        

if __name__ == "__main__":
    start_game()