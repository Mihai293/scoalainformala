import csv
from prettytable import PrettyTable
import datetime
import pandas as pd
continuare1 = "y"
continuare = "y"
task_list = []
categorii_list = []
categorii = ["munca", "curs", "friends"]

def validare_data(data):
    try:
        datetime.datetime.strptime(data, "%d-%m-%y-%H:%M")

    except ValueError as e :
        print("Eroare data.Acest task nu este salvat !")
        return False
    return True

def interogare():
    global continuare

    while continuare == "y":
        categorii = ["munca", "curs", "friends"]
        task = input("Introducere task :")
        limita = input("Introducere data limita :")
        if validare_data(limita) is not True:
            break
        utilizator = input("Introducere utilizator :")
        categorie = input("Introducere categorie :")
        if categorie not in categorii :
            print("ERR categorie, task nu a fost introdus")
            break

        with open('task', 'a') as csv_file:
            scriere_csv1 = csv.writer(csv_file, delimiter=",")
            scriere_csv1.writerow([task, limita, utilizator, categorie])
        with open('categorie', 'a') as csv_file:
            scriere_csv = csv.writer(csv_file, delimiter=",")
            scriere_csv.writerow([categorii])
        continuare = input("Doresti sa introduci un alt task ? y/n ?")
        pass

    return True


def meniu():
    global continuare1
    while continuare1 == "y":
        x = PrettyTable()
        x.field_names = ["Key", "Varianta"]
        x.add_row(["1","sortare ascendentă task"])
        x.add_row(["2","sortare descendentă task"])
        x.add_row(["3","sortare ascendentă data"])
        x.add_row(["4","sortare descendentă data"])
        x.add_row(["5","sortare ascendentă persoana responsabilă"])
        x.add_row(["6","sortare descendentă persoană responsabilă"])
        x.add_row(["7","sortare ascendentă categorie"])
        x.add_row(["8","sortare descendentă categorie"])
        x.add_row(["9","filtrare task"])
        x.add_row(["10","filtrare data"])
        x.add_row(["11","filtrare persoana responsabila"])
        x.add_row(["12","filtrare categorie"])
        x.add_row(["13","editare task"])
        x.add_row(["14","sterge task"])
        print(x)
        alegere = input("Press your Key: ")

        if alegere == "1":
            with open("task", "r") as file:
                sort_task = file.readlines()

                for x in sorted(sort_task, key=lambda x: x.split(",")[0]):
                    print(x)

        elif alegere == "2":
            with open("task", "r") as file:
                sort_task = file.readlines()
                for x in sorted(sort_task, key=lambda x: x.split(",")[0], reverse=True):
                    print(x)

        elif alegere == "3":
            filtered_df = pd.read_csv("task", header=None)
            filtered_df.sort_values(by=[1],ascending=False, inplace= True)
            print(filtered_df)


        elif alegere == "4":
            filtered_df = pd.read_csv("task", header=None)
            filtered_df.sort_values(by=[1], ascending=False, inplace=True)
            print(filtered_df)

        elif alegere == "5":
            with open("task", "r") as file:
                sort_responsabil = file.readlines()
                for x in sorted(sort_responsabil, key=lambda x: x.split(",")[2:]):
                    print(x)

        elif alegere == "6":
            with open("task", "r") as file:
                sort_responsabil = file.readlines()
                for x in sorted(sort_responsabil, key=lambda x: x.split(",")[2:], reverse=True):
                    print(x)

        elif alegere == "7":
            with open("task", "r") as file:
                sort_categorie = file.readlines()
                for x in sorted(sort_categorie, key=lambda x: x.split(",")[-1]):
                    print(x)

        elif alegere == "8":
            with open("task", "r") as file:
                sort_categorie = file.readlines()
                for x in sorted(sort_categorie, key=lambda x: x.split(",")[-1],reverse=True):
                    print(x)

        elif alegere == "9":
            filtered_df = pd.read_csv("task", usecols=[0])
            print(filtered_df)

        elif alegere == "10":
            filtered_df = pd.read_csv("task", usecols=[1])
            print(filtered_df)

        elif alegere == "11":
            filtered_df = pd.read_csv("task", usecols=[2])
            print(filtered_df)

        elif alegere == "12":
            filtered_df = pd.read_csv("task", usecols=[3])
            print(filtered_df)

        elif alegere == "13":
            edit()

        elif alegere == "14":
            delete()

        print('After sorting')
        continuare1 = input("Doresti sa introduci o alta operatiune ? y/n ?")


def edit():
    print("To do list :")
    filtered_df = pd.read_csv("task", header=None)
    print(filtered_df)
    alegere = int(input("Alege randul, conform index, pe care vrei sa-l editezi !"))
    alegere1 = int(input("Alege coloana, conform index, pe care vrei sa-l editezi !"))

    filtered_df.loc[alegere,alegere1] = input("Schimbi cu : ")
    filtered_df.to_csv("task", index=False)

    print(filtered_df)

def delete():
    print("To do list :")
    filtered_df = pd.read_csv("task", header=None)
    print(filtered_df)
    alegere = int(input("Alege randul, conform index, pe care vrei sa-l stergi !"))

    filtered_df.drop(labels=[alegere], axis=0, inplace=True)
    filtered_df.to_csv("task", index=False)
    print(filtered_df)

interogare()
meniu()

