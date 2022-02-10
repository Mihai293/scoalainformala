import random

start = (input("Vrei sa incepi ? y / n : ")).lower()
start_y = "y"
symbol_player = "0   "
symbol_pc = "X   "
board = {'7': None, '8': None, '9': None,
         '4': None, '5': None, '6': None,
         '1': None, '2': None, '3': None}

if start == start_y :
    print("Ai prima mutare, succes !")
    alegere = input("Alege un numar de la 1 la 9 : ")

    #board[alegere] = symbol_player

    while None in list(board.values()) :
        if alegere is None :
            alegere = input("Alege un numar de la 0 la 9 : ")
        board[alegere] = symbol_player
        alegere = None

        if board["5"] is None :
            board["5"] = symbol_pc
        elif board["1"] is None :
            board["1"] = symbol_pc
        elif board["3"] is None :
            board["3"] = symbol_pc
        elif board["7"] is None :
            board["7"] = symbol_pc
        elif board["9"] is None :
            board["9"] = symbol_pc
        elif board["6"] is None :
            board["6"] = symbol_pc
        elif board["4"] is None :
            board["4"] = symbol_pc
        elif board["2"] is None:
            board["2"] = symbol_pc
        elif board["8"] is None :
            board["8"] = symbol_pc

        print(f"{board['7']}, {board['8']}, {board['9']}\n"
              f"{board['4']}, {board['5']}, {board['6']}\n"
              f"{board['1']}, {board['2']}, {board['3']}")

        if board["1"] == board["2"] == board["3"] != None :
            if board ["1"] == symbol_player:
                print("Ai castigat  !")
                break
            else :
                print("Ai pierdut  !")
                break
        if board["4"] == board["5"] == board["6"] != None:
            if board["4"] == symbol_player:
                print("Ai castigat !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["8"] == board["9"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["1"] == board["5"] == board["9"] != None:
            if board["1"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["5"] == board["3"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["4"] == board["1"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["8"] == board["5"] == board["2"] != None:
            if board["8"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["9"] == board["6"] == board["3"] != None:
            if board["9"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break

else:
    print("pc ul incepe")
    if None in list(board.values()):
        board ['5'] = symbol_pc
    print(f"{board['7']}, {board['8']}, {board['9']}\n"
          f"{board['4']}, {board['5']}, {board['6']}\n"
          f"{board['1']}, {board['2']}, {board['3']}")

    alegere = input("Alege un numar de la 1 la 9 : ")
    while alegere == "5":
        print("Pozitia este aleasa de pc, te rog alege alta varianta ! ")
        alegere = input("Alege un numar de la 1 la 9 : ")


    while symbol_pc in list(board.values()):
        if alegere is False :
            alegere = input("Alege un numar de la 1 la 9 : ")
        board[alegere] = symbol_player
        alegere = False

        if board["1"] == board["2"] == board["3"] != None :
            if board ["1"] == symbol_player:
                print("Ai castigat  !")
                break
            else :
                print("Ai pierdut  !")
                break
        if board["4"] == board["5"] == board["6"] != None:
            if board["4"] == symbol_player:
                print("Ai castigat !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["8"] == board["9"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["1"] == board["5"] == board["9"] != None:
            if board["1"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["5"] == board["3"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["4"] == board["1"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["8"] == board["5"] == board["2"] != None:
            if board["8"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["9"] == board["6"] == board["3"] != None:
            if board["9"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break

        if board["1"] is None :
            board["1"] = symbol_pc
        elif board["3"] is None :
            board["3"] = symbol_pc
        elif board["7"] is None :
            board["7"] = symbol_pc
        elif board["9"] is None :
            board["9"] = symbol_pc
        elif board["6"] is None :
            board["6"] = symbol_pc
        elif board["4"] is None :
            board["4"] = symbol_pc
        elif board["2"] is None:
            board["2"] = symbol_pc
        elif board["8"] is None :
            board["8"] = symbol_pc

        print(f"{board['7']}, {board['8']}, {board['9']}\n"
              f"{board['4']}, {board['5']}, {board['6']}\n"
              f"{board['1']}, {board['2']}, {board['3']}\n")

        if board["1"] == board["2"] == board["3"] != None :
            if board ["1"] == symbol_player:
                print("Ai castigat  !")
                break
            else :
                print("Ai pierdut  !")
                break
        if board["4"] == board["5"] == board["6"] != None:
            if board["4"] == symbol_player:
                print("Ai castigat !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["8"] == board["9"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["1"] == board["5"] == board["9"] != None:
            if board["1"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["5"] == board["3"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["7"] == board["4"] == board["1"] != None:
            if board["7"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["8"] == board["5"] == board["2"] != None:
            if board["8"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break
        if board["9"] == board["6"] == board["3"] != None:
            if board["9"] == symbol_player:
                print("Ai castigat  !")
                break
            else:
                print("Ai pierdut  !")
                break



