# Number of lines
board = {1: "|1|2|3|4|5|\n",
        2: "|#|#|#|#|#|\n",
        3: "|#|#|#|#|#|\n",
        4: "|#|#|#|#|#|\n",
        5: "|#|#|#|#|#|\n",
        6: "|#|#|#|#|#|\n"}
player = ""
amount = int(input("How many player's do you want to play with?"))
def player_setter(player, amount):
    i = 0
    while i < amount:
        temp_player = input(f"What character do you want player {len(player)+1} to be?")
        while len(temp_player) > 1:
            print("Sorry, you can only set one character to your player.")
            temp_player = input(f"What character do you want player {len(player)+1} to be?")
        player += temp_player
        print(player)
        i+=1
    return player

def print_board(board):
    i = 1
    printed_board = '\n'
    while i <= len(board):
        printed_board += board[i]
        i+=1
    return printed_board

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
        return
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

def main(player_number):
    if player_number >= len(player):
        player_number = 0
    print(print_board(board))
    user = 0
    while user not in (1,2,3,4,5):
        user = input('What column would you like to drop your piece in?\n')
        try:
            user = int(user)
            if user not in (1,2,3,4,5):
                print(f"Error: '{user}' not in range 1-5\n")
        except Exception as e:
            print(f"Error: '{user}' not in range 1-5\n")
    replace(lowest_unoccupied_line(user, board), user, board, player_number, player)
    player_number += 1
    main(player_number)
player_number = 0
player = player_setter(player, amount)
main(player_number)
