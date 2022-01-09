# Number of lines


board = {1: "|1|2|3|4|5|6|7|\n",
        2: "|#|#|#|#|#|#|#|\n",
        3: "|#|#|#|#|#|#|#|\n",
        4: "|#|#|#|#|#|#|#|\n",
        5: "|#|#|#|#|#|#|#|\n",
        6: "|#|#|#|#|#|#|#|\n",
        7: "|#|#|#|#|#|#|#|\n"}

player = ""

player_number = 0

amount = ""

def start_screen(amount, player = ""):
    try:
        amount = int(input("How many player's do you want to play with?\n")) #amount currently only gets set if the first input is a number. If it isn't, it will throw the exception and go back through the function, but won't actually set it to a number the second+ time through.
    except Exception as f:
        print (f"The amount of players '{amount}' must be a number")
        start_screen(amount)
    player = player_setter(player, amount)
    return player

def player_setter(player, amount):
    i = 0
    while i < int(amount):
        temp_player = input(f"What character do you want player {len(player)+1} to be?\n")
        while len(temp_player) > 1 or temp_player in player:
            if len(temp_player) > 1:
                print("Sorry, you can only set one character to your player.")
                temp_player = input(f"What character do you want player {len(player)+1} to be?\n")
            if temp_player in player:
                print(f"Sorry, '{temp_player}' is already a used character by another player.")
                temp_player = input(f"What character do you want player {len(player)+1} to be?\n")
        player += temp_player
        i+=1
    return player

def create_board(board = {}):
    rows = input("How many rows do you want to play with? (Default is 6)")
    columns = input("How many columns do you want to play with? (Default is 7)")
    in_a_row = input("How many slots in a row to win? (Default is 4)") # Might need some rewording


def print_board(board):
    i = 1
    printed_board = '\n'
    while i <= len(board):
        printed_board += board[i]
        i+=1
    return printed_board

def score():
    pass

def lowest_unoccupied_line(column, board):
    line = len(board)
    lowest_line = 5
    while line >= 1:
        str_line = board[line]
        if str_line[column*2-1] != "#":
            line-=1
        else:
            lowest_line = line
            return lowest_line

def replace(line, column, board, player_number, player):
    try:
        str_line = board[line]
    except Exception as e:
        print(f"Oops! Column {column} is already full! Pick a different column.\n")
        return False
    i = 0
    new_str_line = ''
    while i < len(str_line):
        if i == column*2-1:
            new_str_line += player[player_number]
        else:
            new_str_line += str_line[i]
        i+=1
    board[line] = new_str_line
    return board[line]

def main(player_number, player):
    if player_number >= len(player):
        player_number = 0
    print(print_board(board))
    user = 0
    while user not in range(1,len(board)+1):
#   while user not in (1,2,3,4,5,6,7):
        user = input('What column would you like to drop your piece in?\n')
        try:
            user = int(user)
            if user not in range(1,len(board)+1):
#           if user not in (1,2,3,4,5,6,7):
                print(f"Error: '{user}' not in range 1-{len(board)}\n")
        except Exception as e:
            if user == "q":
                print ("goodbye")
            else:
                print(f"Error: '{user}' not in range 1-{len(board)}\n")
    check = replace(lowest_unoccupied_line(user, board), user, board, player_number, player)
    if check != False:
        player_number += 1
    main(player_number, player)

# Line below this has to stay outside of main() otherwise it gets called multiple times and we only want it to get called once.
player = start_screen(amount, player)
main(player_number, player)
