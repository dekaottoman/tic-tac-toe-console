#The table we play on
table = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Function to display table
def display_table():
    print("|" + table[0] + "|" + table[1] + "|" + table[2] + "|")
    print("|" + table[3] + "|" + table[4] + "|" + table[5] + "|")
    print("|" + table[6] + "|" + table[7] + "|" + table[8] + "|")

#Function to make plays
def insert(turn):
    print("Turn of " + turn)
    index = input("Enter Index : ")
    
    #Type "exit" to exit
    if(index == "exit"):
        exit(0)

    table[int(index) - 1] = turn

#Function to check if there is a horizontal winner
def check_win_h():
    win = False

    #Row 1
    if(table[0] != "-"):
        if(table[0] == table[1]):
            if(table[0] == table[2]):
                win = True
    #Row 2
    if(table[3] != "-"):
        if(table[3] == table[4]):
            if(table[3] == table[5]):
                win = True
    #Row 3
    if(table[6] != "-"):
        if(table[6] == table[7]):
            if(table[6] == table[8]):
                win = True

    return win

#Function to check if there is a vertical winner
def check_win_v():
    win = False

    #Column 1
    if(table[0] != "-"):
        if(table[0] == table[3]):
            if(table[0] == table[6]):
                win = True

    #Column 2
    if(table[1] != "-"):
        if(table[1] == table[4]):
            if(table[1] == table[7]):
                win = True

    #Column 3
    if(table[2] != "-"):
        if(table[2] == table[5]):
            if(table[2] == table[8]):
                win = True

    return win

#Function to check if there is a diagonal winner
def check_win_d():
    win = False

    #Diagonal 1
    if(table[0] != "-"):
        if(table[0] == table[4]):
            if(table[0] == table[8]):
                win = True

    #Diagonal 2
    if(table[2] != "-"):
        if(table[2] == table[4]):
            if(table[2] == table[6]):
                win = True

    return win

#Function to check draws
def check_draw(turn_count):
    if(turn_count < 9):
        return False
    else:
        return True

#Function to initiate the game
def play():
    game = True
    turn_count = 0
    turn = "X"
    print("WELCOME TO TIC TAC TOE!!!")
    print("(by @dekaottoman, type 'exit' to exit)\n")
    while game:
        display_table()
        insert(turn)
        turn_count += 1

        #Win check (Horizontal)
        if check_win_h():
            display_table()
            print(turn + " Wins !!!")
            input()
            exit(0)

        #Win check (Vertical)
        if check_win_v():
            display_table()
            print(turn + " Wins !!!")
            input()
            exit(0)

        #Win check (Diagonal)
        if check_win_d():
            display_table()
            print(turn + " Wins !!!")
            input()
            exit(0)

        #Draw check
        if check_draw(turn_count):
            display_table()
            print("Draw !!!")
            input()
            exit(0)

        if(turn == "X"):
            turn = "O"
        else:
            turn = "X"

play()