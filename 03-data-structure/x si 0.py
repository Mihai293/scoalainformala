import random
choice = int(input("Alege un numar intre 0 si 9  --> "))

x = random.randrange(0,9)
simbol_calculator = 0
simbol_utilizator = 'X'

if choice >= x:
    print("Ai castigat, tu incepi ! ")
    simbol_utilizator = 0
    simbol_calculator = 'X'

Board = {'7': None, '8': None, '9': None,
         '4': None, '5': None, '6': None,
         '1': None, '2': None, '3': None}

board_keys = []

for key in Board:
    board_keys.append(key)
else:
    print("Ai pierdut, PC-ul va incepe")

Lista = ["Player", "Computer"]
index = input("Alege un numar intre 0 si 9  --> ")
Board[index] = simbol_utilizator
while None in list(Board.values()):
    if index is None:
        index = input("Alege un numar intre 0 si 9  --> ")
    Board[index] = simbol_utilizator
    index = None
    print(Board)