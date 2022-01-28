# Number of lines
# using tabs instead of 4 spaces

#check for the max score to win
#
#
#
#
#
#

board = {0: "|1|2|3|4|5|6|7|\n",
        1: "|#|#|#|#|#|#|#|\n",
        2: "|#|#|#|#|#|#|#|\n",
        3: "|#|#|#|#|#|#|#|\n",
        4: "|#|#|#|#|#|#|#|\n",
        5: "|#|#|#|#|#|#|#|\n",
        6: "|#|#|#|#|#|#|#|\n"}

player = ""

top_line = ""

player_number = 0

amount = ""

rows = 0

columns = 0

in_a_row = 0

def start_screen(amount = "", player = ""):
    rows = set_rows()
    columns = set_columns()
    in_a_row = set_score(rows, columns)
    amount = set_player_number(amount, rows, columns, in_a_row)
    player = player_setter(player, amount)
    board = create_board(rows, columns, in_a_row)
    return player, board, rows, columns

def set_rows(rows = ""):
    rows = input("How many rows do you want to play with? (Default is 6)\n")
    if rows == "":
        rows = 6
    else:
        try:
            rows = int(rows)
        except Exception as f:
            print (f"The amount of rows '{rows}' must be a number")
            set_rows()
    return rows

def set_columns(columns = ""):
    columns = input("How many columns do you want to play with? (Default is 7)\n")
    if columns == "":
        columns = 7
    else:
        try:
            columns = int(columns)
        except Exception as f:
            print (f"The amount of columns '{columns}' must be a number")
            set_columns()
    return columns

def set_score(rows, columns, in_a_row = ""):
    if rows > columns:
        print(f"columns: {columns}")
        print(f"rows: {rows}")
        max_score = rows
    else:
        print(f"columns: {columns}")
        print(f"rows: {rows}")
        max_score = columns
    in_a_row = input(f"What is the score to win? The maximum possible is {max_score} (Default is 4)\n") # Might need some rewording (how many spots in a row to win?)
    if in_a_row == "":
        in_a_row = 4
    else:
        try:
            in_a_row = int(in_a_row)
        except Exception as f:
            print (f"The score to win '{in_a_row}' must be a number")
            set_score(rows, columns)
        if in_a_row > max_score:
            print("That value is above the maximum score limit. If you wish to increase this, increase the boards columns or rows.\n")
            set_score(rows, columns)
    return in_a_row
#        in_a_row = int(in_a_row)
def set_player_number(amount, rows, columns, in_a_row):
    amount = input(f"How many player's do you want to play with? the maximum value is {int((rows*columns)/in_a_row)}\n")
    if amount == "":
        amount = 2
    else:
        try:
            amount = int(amount) #amount currently only gets set if the first input is a number. If it isn't, it will throw the exception and go back through the function, but won't actually set it to a number the second+ time through.
        except Exception as f:
            print (f"The amount of players '{amount}' must be a number")
            set_player_number(amount, rows, columns, in_a_row)
        if amount > ((rows*columns)/in_a_row):
            print("That many players can not possibley fit on this board")
            set_player_number(amount, rows, columns, in_a_row)
    return amount

def player_setter(player, amount):
    i = 0
    while i < int(amount):
        temp_player = input(f"What character do you want player {len(player)+1} to be?\n")
        if temp_player == "#":
            print("player can not be \"#\"")
        else:
            if temp_player == "":
                temp_player = f"{len(player)}"
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

def create_board(top_line = "", rows = 6, columns = 7, in_a_row = 4, board = {}):
    for i in range(columns):
        string += ("#")
        print(string)
        top_line += f"{i + 1}"
    string += "/n"
    top_line += "/n"
    for i in range(rows):
        board[i] = string
        print(board)
    return board


#    i = 0
#    string = "|"
#    string_num = "|"
#    while i <= columns - 1:
#        if i > 98:
#            string += "  #|"
#        elif i > 8:
#            string += " #|"
#        else:
#            string += "#|"
#        print(string)
#        string_num += f"{i + 1}|"
#        i += 1
#    string += "\n"
#    string_num += "\n"
#    board[0] = string_num
#    i = 1
#    while i <= rows:
#        board[i] = string
#        print(board)
#        i += 1
#    return board


def print_board(board):
    i = 0
    printed_board = '\n'
    while i < len(board):
        print(f"pb = {printed_board}\nb = {board}\ni = {i}") #dude your code is borked
        printed_board += board[i]
        i+=1
    return printed_board

def score():
    pass
#1 rework the board to not have the | inbetween the #'s and it is just #'s
#2 change the print board function to print the board but with |'s inbetween the #'s
    back_score = 1 # for scoring in the \ direction
    fore_score = 1 # for scoring in the / direction
    lon_score = 1 # for scoring in the | direction
    lat_score = 1 # for scoring in the - direction
#have to learn how to index dictionaries again:
    char = board[line]
    temp = char[place_col]
    for i in range(4):
        if i == 0:
            direction = "back"
            chng_col = 1
            chng_row = 1
        elif i == 1:
            directoon = "fore"
            chng_col = 1
            chng_row = -1
        elif i == 2:
            direction = "lon"
            chng_col = 0
            chng_row = 1
        elif i == 3:
            directon = "lat"
            chng_col = 1
            chng_row = 0
        else:
            direction = "back"
            chng_col = 1
            chng_row = 1
        srt_chng_col = chng_col
        srt_chng_row = chng_row
        for i in range(in_a_row):
            while board[line+chng_row:place_col+chng_col] == temp:
                chng_col += srt_chng_col
                chng_row += srt_chng_row
                if direction == back:
                    back_score += 1
                elif direction == fore:
                    fore_score += 1
                elif direction == lon:
                    lon_score += 1
                else:
                    lat_score += 1
            chng_col = srt_chng_col
            chng_row = srt_chng_row
            while board[line-chng_row:place_col-chng_col] == temp:
                chng_col += srt_chng_col
                chng_row += srt_chng_row
                if direction == back:
                    back_score += 1
                elif direction == fore:
                    fore_score += 1
                elif direction == lon:
                    lon_score += 1
                else:
                    lat_score += 1
    if back_score >= in_a_row or fore_score >= in_a_row or lon_score >= in_a_row or lat_score >= in_a_row:
        print (f"Player (change to winner) won!")

def lowest_unoccupied_line(column, board):
    line = len(board)-1
    lowest_line = 5
    str_line = ""
    while line >= 1:
        print(f"str_line = {str_line}\nboard = {board}\nline = {line}")
        str_line = board[line]
        if str_line[column*2-1] != "#":
            line-=1
        else:
            lowest_line = line
            return lowest_line
board
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
    place_col = 0
    while place_col not in range(1,len(board)+1):
#   while place_col not in (1,2,3,4,5,6,7):
        place_col = input('What column would you like to drop your piece in?\n')
        try:
            place_col = int(place_col)
            if place_col not in range(1,len(board)+1):
#           if place_col not in (1,2,3,4,5,6,7):
                print(f"Error: '{place_col}' not in range 1-{len(board)}\n")
        except Exception as e:
            if place_col == "q":
                print ("Goodbye")
                return
            else:
                print(f"Error: '{place_col}' not in range 1-{len(board)}\n")
    check = replace(lowest_unoccupied_line(place_col, board), place_col, board, player_number, player)
    if check != False:
        player_number += 1
    main(player_number, player)

# Line below this has to stay outside of main() otherwise it gets called multiple times and we only want it to get called once. now i am trying to see how far this goes off the screen before it stops me. EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE it dosent stop me, it just makes the screen go over
player, board, rows, columns = start_screen(amount, player)
main(player_number, player)
