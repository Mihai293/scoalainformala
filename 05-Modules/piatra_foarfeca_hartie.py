import random

player1 = input(f"Care este numele tau? ")

while True:

    # player1 = input(f"Care este numele tau? ")

    optiuni = ["piatra", "hartie", "foarfeca"]

    print(f"Salut {player1}, optiunile tale sunt: {optiuni} ")

    player_choice = input("Alege o varianta: ").lower()

    calculator = random.choice(optiuni)
    print(f"Calculatorul a ales {calculator}")
    if player_choice == calculator:
        print("Egalitate, reia jocul.")

    elif player_choice == "piatra":
        if calculator == "hartie":
            print("Ai priedut.")
        else:
            print("Ai castigat")

    elif player_choice == "hartie":
        if calculator == "piatra":
            print("Ai castigat.")
        else:
            print("Ai pierdut")

    elif player_choice == "foarfeca":
        if calculator == "hartie":
            print("Ai castigat.")
        else:
            print("Ai pierdut")



    repetare = input("Vrei sa joci again? y/n ")

    if repetare == "n":
        break



