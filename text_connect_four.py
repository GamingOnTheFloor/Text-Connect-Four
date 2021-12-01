# Number of lines
board = {1: "|1|2|3|4|5|\n",
        2: "|#|#|#|#|#|\n",
        3: "|#|#|#|#|#|\n",
        4: "|#|#|#|#|#|\n",
        5: "|#|#|#|#|#|\n",
        6: "|#|#|#|#|#|\n"}
def print_board(board):
    i = 1
    printed_board = '\n'
    while i <= len(board):
        printed_board += board[i]
        i+=1
    return printed_board

def lowest_unoccupied_line(colum, board):
    line = len(board)
    lowest_line = 5
    while line >= 1:
        str_line = board[line]
        if str_line[colum*2-1] != "#":
            line-=1
        else:
            lowest_line = line
            return lowest_line

def replace(line, colum, board):
    try:
        str_line = board[line]
    except Exception as e:
        print(f"Oops! Colum {colum} is already full! Pick a different colum.\n")
        return
    i = 0
    new_str_line = ''
    while i < len(str_line):
        if i == colum*2-1:
            new_str_line += "X"
        else:
            new_str_line += str_line[i]
        i+=1
    board[line] = new_str_line
    return board[line]
    
def main():
    print(print_board(board))
    user = 0
    while user not in (1,2,3,4,5):
        user = input('What colum would you like to drop your piece in?\n')
        try:
            user = int(user)
            if user not in (1,2,3,4,5):
                print(f"Error: '{user}' not in range 1-5\n")
        except Exception as e:
            print(f"Error: '{user}' not in range 1-5\n")
    replace(lowest_unoccupied_line(user, board), user, board)
    main()
main()
