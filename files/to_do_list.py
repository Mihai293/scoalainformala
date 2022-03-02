import csv
from prettytable import PrettyTable
continuare = "y"
task_list = []
categorii_list = []
categorii = ["munca", "curs", "friends"]

def tabel():
    x = PrettyTable()
    x.field_names = ["Task", "Limita", "User", "Categorie"]

    print(x)


def interogare():
    global continuare
    while continuare == "y":
        categorii = ["munca", "curs", "friends"]
        categorii_list.append(categorii)
        task = input("Introducere task :")
        task_list.append(task)
        limita = input("Introducere data limita :")
        task_list.append(limita)
        utilizator = input("Introducere utilizator :")
        task_list.append(utilizator)
        categorie = input("Introducere categorie :")

        if categorie not in categorii :
            print("ERR categorie")
            break

        with open('task', 'w') as csv_file:
            scriere_csv1 = csv.writer(csv_file, delimiter=",")
            scriere_csv1.writerow(task_list)


        with open('categorie', 'a') as csv_file:
            scriere_csv = csv.writer(csv_file, delimiter=",")
            scriere_csv.writerow(categorii_list)

        continuare = input("Doresti sa introduci un alt task ? y/n ?")
        if continuare == "y":
            task_list.append("\n")
    return True


interogare()

def meniu():
    meniu1 = {"1": "sortare ascendentă task",

    "2": "sortare descendentă task",

    "3": "sortare ascendentă data",

    "4": "sortare descendentă data",

    "5": "sortare ascendentă persoana responsabilă",

    "6": "sortare descendentă persoană responsabilă",

    "7": "sortare ascendentă categorie",

    "8": "sortare descendentă categorie"
             }

# print(meniu)
# alegere_meniu = input("Number: ")
# task_sortati = sorted(task_list, key=lambda ux : task_list[0])
# print(task_sortati)

#loads and dumps
#categoriile existente df.to_csv('my_csv.csv', mode='a', header=False)
