import random

start = (input("Vrei sa incepi ? y / n : ")).lower()
start_y = "y"
symbol_player = 0
symbol_pc = "X"
board = {'7': None, '8': None, '9': None,
         '4': None, '5': None, '6': None,
         '1': None, '2': None, '3': None}
board_list = []


if start == start_y :
    print("Ai prima mutare, succes !")
    alegere = input("Alege un numar de la 1 la 9 : ")

    board[alegere] = symbol_player

    while None in list(board.values()) :
        if alegere is None :
            alegere = input("Alege un numar de la 0 la 9 : ")
        board[alegere] = symbol_player
        alegere = None
        print(board)

else:
    print("pc ul incepe")