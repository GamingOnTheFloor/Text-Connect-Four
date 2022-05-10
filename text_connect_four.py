import time

# using tabs instead of 4 spaces

    #to do list:
# make an ai using weighted variables that predicts where the player is going to go next by calculating probability

board = {0: "#######/n",
         1: "#######/n",
         2: "#######/n",
         3: "#######/n",
         4: "#######/n",
         5: "#######/n"}
player = ""
top_line = ""
player_number = 0
amount = ""
rows = 0
columns = 0
in_a_row = 0
play = True
line = 0
round = 0
AIc = -1
AIp = ""

def start_screen(amount = "", player = ""):
    rows = set_rows()
    print(f"Rows is set to {rows}.\n")
    columns = set_columns()
    print(f"Columns is set to {columns}.\n")
    in_a_row = set_score(rows, columns)
    print(f"Score to win is {in_a_row}.\n")
    amount = set_player_number(amount, rows, columns, in_a_row)
    print(f"You are playing with {amount} players.\n")
    player = player_setter(player, amount)
    print(f"Player characters are: {player}\n")
    AIc = -1
    AIp = ""
    while AIc < 0 or AIc > int((rows * columns) / in_a_row):
        AIc = int(input(f"How many AI players do you want? There is a maximum of {int(((rows * columns) / in_a_row) - amount)}.\n"))
        if AIc == "":
            if amount == 0:
                AIc = 2
            elif amount == 1:
                AIc = 1
            else:
                AIc = 0
        if AIc < 0:
            print("The number of AI players cant be negative.")
        elif (AIc > int((rows * columns) / in_a_row)):
            print("You cant have that many AI players.")
    AIp = AI_setter(AIp, AIc)
    board = create_board(rows, columns, in_a_row)
    return player, board, rows, columns, in_a_row, AIc, AIp

def set_rows(rows = ""):
    rows = input("How many rows do you want to play with? (Default is 6)\n")
    if rows == "":
        rows = 6
    else:
        try:
            rows = int(rows)
        except Exception as f:
            print(f"The amount of rows '{rows}' must be a number")
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
            print(f"The amount of columns '{columns}' must be a number")
            columns = set_columns(columns)
    return columns

def set_score(rows, columns, in_a_row = ""):
    if rows > columns:
        max_score = rows
    else:
        max_score = columns
    in_a_row = input(f"What is the score to win? The maximum possible is {max_score}. (Default is 4)\n")
    if in_a_row == "":
        if max_score > 4:
            in_a_row = 4
        else:
            in_a_row = max_score
    else:
        try:
            in_a_row = int(in_a_row)
        except Exception as f:
            in_a_row = set_score(rows, columns, in_a_row)
        if in_a_row > max_score:
            in_a_row = set_score(rows, columns, in_a_row)
    return in_a_row

def set_player_number(amount, rows, columns, in_a_row):
    good = False
    while good == False:
        amount = input(f"How many player's do you want to play with? The maximum player count is {int((rows*columns)/in_a_row)}.\n")
        if amount == "":
            if int((rows * columns) / in_a_row) > 2:
                amount = 2
                good = True
            else:
                amount = int((rows * columns) / in_a_row)
                good = True
        elif amount == 0:
            print("There must be at least one player.")
            good = False
        else:
            try:
                amount = int(amount)
                good = True
            except Exception as f:
                print(f"The amount of players '{amount}' must be a number")
                amount = set_player_number(amount, rows, columns, in_a_row)
            if amount > ((rows * columns) / in_a_row):
                print("That many players can not possibley fit on this board")
                amount = set_player_number(amount, rows, columns, in_a_row)
    return amount

def player_setter(player, amount):
    for i in range(amount):
        temp_player = input(f"What character do you want player {len(player) + 1} to be?\n")
        if temp_player == "#":
            print("Player can not be '#'")
        else:
            if temp_player == "":
                temp_player = f"{len(player)}"
            while len(temp_player) > 1 or temp_player in player:
                if len(temp_player) > 1:
                    print("Sorry, you can only set one character to your player.")
                    temp_player = input(f"What character do you want player {len(player) + 1} to be?\n")
                if temp_player in player:
                    print(f"Sorry, '{temp_player}' is already a used character by another player.")
                    temp_player = input(f"What character do you want player {len(player) + 1} to be?\n")
            player += temp_player
            i += 1
    return player

def AI_setter(AIp, AIc):
    total_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz()[]{}<>-~=+_,.;!?:/\\@$%&^*'`\""
    for i in range(AIc):
        try_name = 0
        for j in range(len(total_chars)):
            if total_chars[j] in AIp or total_chars[j] in player:
                try_name += 1
            else:
                AIp += total_chars[j]
                break
    print(f"\nAI characters are: {AIp}\n")
    return AIp

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

def score(board, line, place_col, in_a_row, player_number, play, rows, columns):
    back_score = -1
    fore_score = -1
    lon_score = -1
    lat_score = -1
    place_col -= 1
    stupid_thing = True
    y = board[line]
    xy = y[place_col]
    for i in range(4):
        if i == 0:
            direction = "back" # IS DOWN-RIGHT
            srt_chng_col = 1
            srt_chng_row = 1
        elif i == 1:
            direction = "fore" # IS DOWN-LEFT
            srt_chng_col = -1
            srt_chng_row = 1
        elif i == 2:
            direction = "lon" # IS DOWN
            srt_chng_col = 0
            srt_chng_row = 1
        elif i == 3:
            direction = "lat" # IS RIGHT
            srt_chng_col = 1
            srt_chng_row = 0
        else:
            direction = "back"
            srt_chng_col = 1
            srt_chng_row = 1
        stupid_thing = True
        chng_row, chng_col = 0, 0
        temp_y = y
        temp_xy = temp_y[place_col]
        chng_row, chng_col = 0, 0
        while stupid_thing == True:
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
            try:
                if (place_col + chng_col) < 0:
                    break
                temp_y = board[line + chng_row]
                temp_xy = temp_y[place_col + chng_col]
                if xy == temp_xy:
                    stupid_thing = True
                else:
                    stupid_thing = False
            except Exception as e:
                break
        temp_y = y
        temp_xy = temp_y[place_col]
        chng_row, chng_col = 0, 0
        stupid_thing = True
        while stupid_thing == True:
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
            try:
                if (place_col + chng_col) < 0:
                    break
                temp_y = board[line + chng_row]
                temp_xy = temp_y[place_col + chng_col]
                if xy == temp_xy:
                    stupid_thing = True
                else:
                    stupid_thing = False
            except Exception as e:
                break
    if back_score >= in_a_row or fore_score >= in_a_row or lon_score >= in_a_row or lat_score >= in_a_row:
        print("\n\n")
        print(print_board(board))
        print(f"\nPlayer {player_number + 1} won!")
        play = False
    if round == columns * rows:
        print("\n\n")
        print(print_board(board))
        print(f"\nThe board is full, no one won.")
        play = False
    return play

def lowest_unoccupied_line(column, board):
    line = len(board)-1
    lowest_line = len(board)-1
    str_line = ""
    while line >= 0:
        str_line = board[line]
        if str_line[column-1] != "#":
            line -= 1
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
        i += 1
    board[line] = new_str_line
    return board[line], line

def main(player_number, player, play, line, board, rows, columns, in_a_row, AIc, AIp):
    player, board, rows, columns, in_a_row, AIc, AIp = start_screen(amount, player)
    while play == True:
        for i in range(len(player)):
            try:
                if check != False:
                    print(f"\n\n{print_board(board)}\n")
            except Exception as e:
                print(f"\n\n{print_board(board)}\n")
            place_col = 0
            while place_col not in range(1,columns+1):
                place_col = input(f"What column would player {player_number + 1} ({player[player_number]}) like to drop your piece in?\n")
                try:
                    place_col = int(place_col)
                    if place_col not in range(1,columns+1):
                        print(f"Error: '{place_col}' not in range 1-{columns}\n")
                except Exception as e:
                    if place_col == "q":
                        print("Goodbye")
                        return
                    else:
                        print(f"Error: '{place_col}' not in range 1-{columns}\n")
            check, line = replace(lowest_unoccupied_line(place_col, board), place_col, board, player_number, player)
            play = score(board, line, place_col, in_a_row, player_number, play, rows, columns)
            if check != False:
                player_number += 1
                if player_number >= len(player):
                    player_number = 0
                round += 1
        for i in AIc:

            pass

main(player_number, player, play, line, board, rows, columns, in_a_row, AIc, AIp)
