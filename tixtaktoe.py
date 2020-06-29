dash_board = [" " for i in range(9)]

print(dash_board)

# print the dash board alone

def print_dashboard():
    row1 = "| {} | {} | {} |".format(dash_board[0],dash_board[1],dash_board[2])
    row2 = "| {} | {} | {} |".format(dash_board[3],dash_board[4],dash_board[5])
    row3 = "| {} | {} | {} |".format(dash_board[6],dash_board[7],dash_board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()
#player to enter the symbols
def player_mode(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2
    print("player {}, your turn is now".format(number))
    
    
    choice = int(input("Enter the postion(1-9): ").strip())
    if dash_board[choice-1] == " ":
        dash_board[choice-1] = icon
    else:
        print("the space is taken !!")
        print("Try for a new position..")
# to check if victory id done
def is_victory(icon):
    if (dash_board[0] == icon and dash_board[1]== icon and dash_board[2]== icon) or \
       (dash_board[3] == icon and dash_board[4]== icon and dash_board[5]== icon) or \
       (dash_board[6] == icon and dash_board[7]== icon and dash_board[8]== icon) or \
       (dash_board[0] == icon and dash_board[4]== icon and dash_board[8]== icon) or \
       (dash_board[2] == icon and dash_board[4]== icon and dash_board[6]== icon) or \
       (dash_board[0] == icon and dash_board[3]== icon and dash_board[6]== icon) or \
       (dash_board[1] == icon and dash_board[4]== icon and dash_board[7]== icon) or \
       (dash_board[2] == icon and dash_board[5]== icon and dash_board[8]== icon):
        return True
    else:
        return False
def is_draw():
    if " " not in dash_board:
        return True
    else:
        return False

#game mode on
while True:

    print_dashboard()
    player_mode("X")
    print_dashboard()
    if is_victory("X"):
        print("Congarts X , you Won !!")
        break
    elif is_draw():
        print("The game is draw now !!!!!")
        break
    player_mode("O")
    if is_victory("O"):
        print_dashboard()
        print("Congarts O , you Won !!")
        break
    elif is_draw():
        print("The game is draw now !!!!!")
        break
    
    
    
    
    
