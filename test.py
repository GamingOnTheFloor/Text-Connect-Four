
board = {0: "%###",
         1: "###%",
         2: "##%#",
         3: "####",
         4: "####",
         5: "####",
         6: "####",
         7: "####",
         8: "####",
         9: "####",
        10: "####",
        11: "####",
        12: "####",
        13: "####",
        14: "####",
        15: "####",
        16: "####",
        17: "#%##",
        18: "#++#",
        19: "#+%#",
        20: "%%+%"}
line = 0
place_col = 1
in_a_row = 3
player_number = "%+"
play = True
rows = 20
columns = 4
play = True

def score(board, line, place_col, in_a_row, player_number, play, rows, columns):
    print("check 2")
    back_score = -1
    fore_score = -1
    lon_score = -1
    lat_score = -1
    place_col -= 1
    stupid_thing = True
    y = board[line]
    xy = y[place_col]
    #if stupid_thing = True:
    for i in range(4):
        #if stupid_thing = True:
        if i == 0:
            direction = "back" # IS DOWN-RIGHT
            srt_chng_col = 1
            srt_chng_row = 1
            print("check 3")
        elif i == 1:
            direction = "fore" # IS DOWN-LEFT
            srt_chng_col = -1
            srt_chng_row = 1
            print("check 4")
        elif i == 2:
            direction = "lon" # IS DOWN
            srt_chng_col = 0
            srt_chng_row = 1
            print("check 5")
        elif i == 3:
            direction = "lat" # IS RIGHT
            srt_chng_col = 1
            srt_chng_row = 0
            print("check 6")
        else:
            direction = "back"
            srt_chng_col = 1
            srt_chng_row = 1
#here on is not working
        stupid_thing = True
        chng_row, chng_col = 0, 0
        #for i in range(in_a_row):
        print(f"in a row 2: {in_a_row}, run {i + 1}")
        temp_y = y
        print(f"temp Y: {temp_y} \nplace col: {place_col}")
        temp_xy = temp_y[place_col]
        chng_row, chng_col = 0, 0
        while stupid_thing == True:
            print(f"\n\nfirst\nxy: {xy}\ntemp_xy: {temp_xy}\n\n")
            if direction == "back":
                back_score += 1
            elif direction == "fore":
                fore_score += 1
            elif direction == "lon":
                lon_score += 1
            else:
                lat_score += 1
            print(f"\n\nback_score: {back_score}\nfore_score: {fore_score}\nlon_score: {lon_score}\nlat_score: {lat_score}\n\n")
            print(f"stupid thing: {stupid_thing}")
            chng_row += srt_chng_row
            chng_col += srt_chng_col
            print(f"{line + chng_row} {line} {chng_row} {srt_chng_row}  {temp_y}")
            try:
            #if line + (-1 * chng_row) > -1 and line + (-1 * chng_row) < rows - 1 and place_col + chng_col > -1 and place_col + chng_col < columns - 1:
                if (place_col + chng_col) < 0:
                    break
                temp_y = board[line + chng_row]
                print(f"Temp_y = {temp_y}")
                temp_xy = temp_y[place_col + chng_col]
                print(f"\n\nsecond\nxy: {xy}\ntemp_xy: {temp_xy}\n\n")
                if xy == temp_xy:
                    stupid_thing = True
                else:
                    stupid_thing = False
            #else:
            #    stupid_thing = False
            except Exception as e:
                print("\n\n\nOOB\n\n\n")
                break
            #print(f"back_score: {back_score}\nfore_score: {fore_score}\nlon_score: {lon_score}\nlat_score: {lat_score}\ntemp_y: {temp_y}\ntemp_xy: {temp_xy}\nxy: {xy}\ny: {y}")
#here not tested good
#1 tab in
        temp_y = y
        print(f"temp Y: {temp_y} \nplace col: {place_col}")
        temp_xy = temp_y[place_col]
        chng_row, chng_col = 0, 0
        stupid_thing = True
        while stupid_thing == True:
            print(f"\n\nfirst\nxy: {xy}\ntemp_xy: {temp_xy}\n\n")
            if direction == "back":
                back_score += 1
            elif direction == "fore":
                fore_score += 1
            elif direction == "lon":
                lon_score += 1
            else:
                lat_score += 1
            print(f"\n\nback_score: {back_score}\nfore_score: {fore_score}\nlon_score: {lon_score}\nlat_score: {lat_score}\n\n")
            print(f"stupid thing: {stupid_thing}")
            chng_row -= srt_chng_row
            chng_col -= srt_chng_col
            print(f"{line + chng_row} {line} {chng_row} {srt_chng_row}  {temp_y}")
            try:
            #if line + (-1 * chng_row) > -1 and line + (-1 * chng_row) < rows - 1 and place_col + chng_col > -1 and place_col + chng_col < columns - 1:
                if (place_col + chng_col) < 0:
                    break
                temp_y = board[line + chng_row]
                print(f"Temp_y = {temp_y}")
                temp_xy = temp_y[place_col + chng_col]
                print(f"\n\nsecond\nxy: {xy}\ntemp_xy: {temp_xy}\n\n")
                if xy == temp_xy:
                    stupid_thing = True
                else:
                    stupid_thing = False
            #else:
            #    stupid_thing = False
            except Exception as e:
                print("\n\n\nOOB\n\n\n")
                break
    if back_score >= in_a_row or fore_score >= in_a_row or lon_score >= in_a_row or lat_score >= in_a_row:
#   if [back_score, fore_score, lon_score, lat_score] >= in_a_row:
        print(print_board(board))
        print(f"Player {player_number + 1} won!")
        play = False
        return play
    print("check 8")

def main(board, line, place_col, in_a_row, player_number, play, rows, columns):
    play = score(board, line, place_col, in_a_row, player_number, play, rows, columns)
    print(board)

main(board, line, place_col, in_a_row, player_number, play, rows, columns)
