amount = ""
rows = 9
columns = 9
in_a_row = 8

def set_player_number(amount, rows, columns, in_a_row):
    good = False
    while good == False:
        max = int((rows*columns)/in_a_row)
        if max > len("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz()[]{}<>-~=+_,.;!?:/\\@$%&^*'`\""):
            max = len("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz()[]{}<>-~=+_,.;!?:/\\@$%&^*'`\"")
        amount = input(f"How many player's do you want to play with? The maximum player count is {max}.\n")
        if amount == "":
            if int((rows * columns) / in_a_row) > 2:
                amount = 2
                good = True
            else:
                amount = int((rows * columns) / in_a_row)
                good = True
        elif amount == '0':
            print("There must be at least one player.")
            good = False
        else:
            try:
                amount = int(amount)
            except Exception as f:
                print(f"The amount of players '{amount}' must be a number")
                good = False
                amount = set_player_number(amount, rows, columns, in_a_row)
            if amount > max:
                print(f"You can't have more than {max} players.")
                good = False
            else:
                break            
    return amount

amount = set_player_number(amount, rows, columns, in_a_row)
print(f"{amount} player(s) to play with.")