# Number of lines
# using tabs instead of 4 spaces

#check for the max score to win
# lowest_unoccupied_line() and replace() aren't working due to us changing how the background board and printed board works. Background board no longer includes |, so we should just need to edit some indexing values.
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

play = True

line = 0

def start_screen(amount = "", player = ""):
    rows = set_rows()
    print(f"Rows is set to {rows}.")
    columns = set_columns()
    print(f"Columns is set to {columns}.")
    in_a_row = set_score(rows, columns)
    print(f"Score to win is {in_a_row}.")
    amount = set_player_number(amount, rows, columns, in_a_row)
    print(f"You are playing with {amount} players.")
    player = player_setter(player, amount)
    print(f"Player characters are: {player}")
    board = create_board(rows, columns, in_a_row)
    return player, board, rows, columns, in_a_row

def set_rows(rows = ""):
    rows = input("How many rows do you want to play with? (Default is 6)\n")
    if rows == "":
        rows = 6
    else:
        try:
            rows = int(rows)
        except Exception as f:
            print (f"The amount of rows '{rows}' must be a number")
            rows = set_rows(rows)
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
            columns = set_columns(columns)
    return columns

def set_score(rows, columns, in_a_row = ""):
    if rows > columns:
        max_score = rows
    else:
        max_score = columns
    in_a_row = input(f"What is the score to win? The maximum possible is {max_score}. (Default is 4)\n") # Might need some rewording (how many spots in a row to win?)
    if in_a_row == "":
        in_a_row = 4
    else:
        try:
            in_a_row = int(in_a_row)
        except Exception as f:
            in_a_row = set_score(rows, columns, in_a_row)
        if in_a_row > max_score:
            in_a_row = set_score(rows, columns, in_a_row)
    return in_a_row

def set_player_number(amount, rows, columns, in_a_row):
    amount = input(f"How many player's do you want to play with? The maximum player count is {int((rows*columns)/in_a_row)}.\n")
    if amount == "":
        amount = 2
    else:
        try:
            amount = int(amount) #amount currently only gets set if the first input is a number. If it isn't, it will throw the exception and go back through the function, but won't actually set it to a number the second+ time through.
        except Exception as f:
            print (f"The amount of players '{amount}' must be a number")
            amount = set_player_number(amount, rows, columns, in_a_row)
        if amount > ((rows*columns)/in_a_row):
            print("That many players can not possibley fit on this board")
            amount = set_player_number(amount, rows, columns, in_a_row)
    return amount

def player_setter(player, amount):
    i = 0
    while i < int(amount):
        temp_player = input(f"What character do you want player {len(player)+1} to be?\n")
        if temp_player == "#":
            print("player can not be '#'")
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

def create_board(rows = 6, columns = 7, in_a_row = 4, board = {}, string = ""):
    for i in range(columns):
        string += ("#")
    string += ""
    for i in range(rows):
        board[i] = string
    return board

def print_board(board):
    top_line = "|"
    for i in range(1,columns+1):
        top_line += f"{i}|"
    top_line += "\n\n"
    printed_board = top_line
    for i in board:
        printed_board += "|"
        for x in board[i]:
            printed_board += f"{x}|"
        printed_board += "\n"
    return printed_board

def score(board, line, place_col, in_a_row, player_number, play):
    print("check 2")
    back_score = 0
    fore_score = 0
    lon_score = 0
    lat_score = 0
    place_col -= 1
    stupid_thing = True
    y = board[line]
    xy = y[place_col]
    for i in range(4):
        if i == 0:
            direction = "back"
            chng_col = 1
            chng_row = 1
            print("check 3")
        elif i == 1:
            directoon = "fore"
            chng_col = 1
            chng_row = -1
            print("check 4")
        elif i == 2:
            direction = "lon"
            chng_col = 0
            chng_row = 1
            print("check 5")
        elif i == 3:
            directon = "lat"
            chng_col = 1
            chng_row = 0
            print("check 6")
        else:
            direction = "back"
            chng_col = 1
            chng_row = 1
#here on is not working
        srt_chng_col = chng_col
        srt_chng_row = chng_row
        for i in range(in_a_row + 1):
            temp_y = y
            print(f"Y: {temp_y} \ncol: {place_col}")
            temp_xy = temp_y[place_col]
            while stupid_thing == True:
                print(f"\n\nxy: {xy}\ntemp_xy: {temp_xy}\n\n")
                if direction == "back":
                    back_score += 1
                elif direction == "fore":
                    fore_score += 1
                elif direction == "lon":
                    lon_score += 1
                else:
                    lat_score += 1
                chng_row += srt_chng_row
                chng_col += srt_chng_col
                temp_y = board[line + (-1 * chng_row)]
                temp_xy = temp_y[place_col + chng_col]
                if xy == temp_xy:
                    stupid_thing = True
                else:
                    stupid_thing = False
                #print (f"back_score: {back_score}\nfore_score: {fore_score}\nlon_score: {lon_score}\nlat_score: {lat_score}\ntemp_y: {temp_y}\ntemp_xy: {temp_xy}\nxy: {xy}\ny: {y}")
#here not tested good
            chng_col = srt_chng_col
            chng_row = srt_chng_row
            print(line + chng_row, line, chng_row, srt_chng_row, temp_y)
            temp_y = board[line + (-1 * chng_row)]
            temp_xy = temp_y[place_col + chng_col]
            print("check 7")
            while temp_xy == xy:
                if direction == "back":
                    back_score += 1
                elif direction == "fore":
                    fore_score += 1
                elif direction == "lon":
                    lon_score += 1
                else:
                    lat_score += 1
                chng_row -= srt_chng_row
                chng_col -= srt_chng_col
                temp_y = y[line + chng_row]
                temp_xy = temp_y[place_col + chng_col]
                print (f"back_score: {back_score}\nfore_score: {fore_score}\nlon_score: {lon_score}\nlat_score: {lat_score}")
            print("check")
    if back_score >= in_a_row or fore_score >= in_a_row or lon_score >= in_a_row or lat_score >= in_a_row:
        print(print_board(board))
        print (f"Player {player_number} won!")
        play = False
    print("check 8")


def lowest_unoccupied_line(column, board):
    line = len(board)-1
    lowest_line = len(board)-1
    str_line = ""
    while line >= 0:
        str_line = board[line]
        if str_line[column-1] != "#":
            line-=1
        else:
            lowest_line = line
            return lowest_line

def replace(line, column, board, player_number, player):
    try:
        str_line = board[line]
    except Exception as e:
        print(f"Oops! Column {column} is already full! Pick a different column.\n")
        return False, False
    i = 0
    new_str_line = ''
    while i < len(str_line):
        if i == column-1:
            new_str_line += player[player_number]
        else:
            new_str_line += str_line[i]
        i+=1
    board[line] = new_str_line
    return board[line], line

def main(player_number, player, play, line):
    while play == True:
        if player_number >= len(player):
            player_number = 0
        print(f"\n\n{print_board(board)}\n")
        place_col = 0
        while place_col not in range(1,columns+1):
    #   while place_col not in (1,2,3,4,5,6,7):
            place_col = input('What column would you like to drop your piece in?\n')
            try:
                place_col = int(place_col)
                if place_col not in range(1,columns+1):
    #           if place_col not in (1,2,3,4,5,6,7):
                    print(f"Error: '{place_col}' not in range 1-{columns}\n")
            except Exception as e:
                if place_col == "q":
                    print ("Goodbye")
                    return
                else:
                    print(f"Error: '{place_col}' not in range 1-{columns}\n")
        check, line = replace(lowest_unoccupied_line(place_col, board), place_col, board, player_number, player)
        score(board, line, place_col, in_a_row, player_number, play)
        if check != False:
            player_number += 1

player, board, rows, columns, in_a_row = start_screen(amount, player)
main(player_number, player, play, line)
