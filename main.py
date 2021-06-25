logo= """
*****************************************************
'   _____ _        _____            _____          
'  |_   _(_)      |_   _|          |_   _|         
'    | |  _  ___    | | __ _  ___    | | ___   ___ 
'    | | | |/ __|   | |/ _` |/ __|   | |/ _ \ / _ \ 
'    | | | | (__    | | (_| | (__    | | (_) |  __/
'    \_/ |_|\___|   \_/\__,_|\___|   \_/\___/ \___|
'                                                  
*****************************************************                                                 
"""
print(logo)

print("            X | O | X    |    7 | 8 | 9 ")
print("           -----------   |   -----------")
print("            O | X | O    |    4 | 5 | 6 ")
print("           -----------   |   -----------")
print("            X | X | O    |    1 | 2 | 3 ")

print("\n\t\t Player A : 'X'  VS  Player B : 'O' ")
print("\n***************************************************** \n")

BOARD = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def drawBoard(board):
    print('\t\t\t\t\t' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("\t\t           -----------")
    print('\t\t\t\t\t' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("\t\t           -----------")
    print('\t\t\t\t\t' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print("\n***************************************************** \n")

def playerMove(player):
    global BOARD
    try:
        player = int(input("\t\tChoose a position from 1~9: \n"))
    except ValueError:
        print("\t\tPlease enter a number between 1 ~ 9")
        player = int(input("\t\tChoose a position from 1~9: \n"))
    finally:
        if player > 9 or player < 1:
            print("\t\tPlease enter a number between 1 ~ 9")
            player = int(input("\t\tChoose a position from 1~9: \n"))
    return player

def check_if_win(moves):
    winning = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for tuple in winning:
        if tuple[0] in moves and tuple[1] in moves and tuple[2] in moves:
            return True
    return False


playerX_moves = []
playerO_moves = []

game_on = True

while game_on:
    X = playerMove(playerX_moves)
    winner = None
    for key, value in BOARD.items():
        if key == X:
            BOARD[key] = 'X'
            drawBoard(BOARD)
            playerX_moves.append(X)
    if check_if_win(playerX_moves):
        winner = "X"
        print(f"The winner is {winner}")
        break
    # print((playerX_moves))

    O = playerMove(playerO_moves)

    for key, value in BOARD.items():
        if key == O:
            BOARD[key] = 'O'
            drawBoard(BOARD)
            playerO_moves.append(O)
    # print(playerO_moves)

    if check_if_win(playerO_moves):
        winner = "O"
        print(f"The winner is {winner}")
        break

    if len(playerX_moves) == 4 and winner == None:
        print("The game is Tie.")
        drawBoard(BOARD)
        break