from random import randint

board = []

for x in range(0, 6):
    board.append(["0"] * 6)

def print_board(board):
    for row in board:
        print(" " .join(row))

print_board(board)

def random_row(board):
    return randint(1, len(board))

def random_col(board):
    return randint(1, len(board[0]))

ship_row = random_row(board)
ship_col = random_col(board)

#print(ship_row)
#print(ship_col)

tries = 10  #Попытки

for turn in range(tries):
    print("Попытка", turn + 1)
    guess_row = int(input("Введите строку: "))
    guess_col = int(input("Введите столбец: "))

    if guess_row == ship_row and guess_col == ship_col:
        print("Ура! Вы подорвали корабль!")
        break
    else:
        if guess_row not in range(1, 7) or \
            guess_col not in range(1, 7):
            print("Такого поля не существует")
        elif board[guess_row-1][guess_col-1] == "X":
            print("Вы уже стреляли в это поле")
        else:
            print("Мима!")
            board[guess_row-1][guess_col-1] = "X"
        if turn == 3:
            print("GAME OVER")
        print_board(board)