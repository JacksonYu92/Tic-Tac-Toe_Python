from instruction import start

start = start()

BOARD = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

def drawBoard(board):
    print('\t\t\t\t\t' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print("\t\t           -----------")
    print('\t\t\t\t\t' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("\t\t           -----------")
    print('\t\t\t\t\t' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    # print("\n***************************************************** \n")

def playerMove(player, opponent, player_moves, opponent_moves):
    global BOARD
    try:
        player_position = int(input(f"\tHi {player}, Please choose a position from 1~9: \n"))
        if player_position in opponent_moves:
            print(f"Sorry, {opponent} already sit on that position, please choose a different position: \n")
            player_position = int(input(f"\tHi {player}, Choose a position from 1~9: \n"))
        elif player_position in player_moves:
            print("Sorry, looks like you already sit on that position, please choose a different position: \n")
            player_position = int(input(f"\tHi {player}, Choose a position from 1~9: \n"))
    except ValueError:
        print("\t\tPlease enter a number between 1 ~ 9")
        player_position = int(input(f"\tHi {player}, Choose a position from 1~9: \n"))
    finally:
        if player_position > 9 or player_position < 1:
            print("\t\tPlease enter a number between 1 ~ 9")
            player_position = int(input(f"\tHi {player}, Choose a position from 1~9: \n"))

    return player_position

def check_if_win(moves):
    winning = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
    for tuple in winning:
        if tuple[0] in moves and tuple[1] in moves and tuple[2] in moves:
            return True
    return False


playerX_moves = []
playerO_moves = []
playerX="X"
playerO="O"


game_on = True

while game_on:
    X = playerMove(playerX,playerO,playerX_moves, playerO_moves)
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

    if len(playerX_moves) > 4 and winner == None:
        print("The game is Tie.")
        break
    else:
        O = playerMove(playerO, playerX,playerO_moves, playerX_moves)

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


