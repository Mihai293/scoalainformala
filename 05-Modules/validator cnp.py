import random
import datetime

cnplist = []


def ss ():
    a = cnplist[0]

    if a == 1 or a == 2:
        return True
    elif a==1:
        print("SEX: M")
    elif a==2:
        print("SEX: F")
    # elif a == 3:
    #     print("SEX: M")
    # elif a==4:
    #     print("SEX: F")
    # elif a==5:
    #     print("SEX: M")
    # elif a == 6:
    #     print("SEX: F")
    # elif a==7:
    #     print("SEX: M")
    # elif a==8:
    #     print("SEX: F")
    # else:
    #     print("Invalid !")
    pass




def aa():
    a = cnplist[1:3]





def ll():
    lunile =  {"01":"Ian","02":"Feb","03":"Mar","04":"Apr","05":"Mai","06":"Iun","07":"Iul","08":"Aug","09":"Sep","10":"Oct","11":"Noi","12":"Dec" }
    a = str(cnplist[3])
    b = str(cnplist[4])
    x = ""
    if a == "0" and b == "1":
        x = "01"
        if x in list(lunile.keys()):
            return True
            #print(lunile[x])
            #print("avem luna")

    elif a == "0" and b == "2":
        x = "02"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "3":
        x = "03"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "4":
        x = "04"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "5":
        x = "05"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "6":
        x = "06"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "7":
        x = "07"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "8":
        x = "08"
        if x in list(lunile.keys()):
            return True

    elif a == "0" and b == "9":
        x = "09"
        if x in list(lunile.keys()):
            return True

    elif a == "1" and b == "0":
        x = "10"
        if x in list(lunile.keys()):
            return True

    elif a == "1" and b == "1":
        x = "11"
        if x in list(lunile.keys()):
            return True

    elif a == "1" and b == "2":
        x = "12"
        if x in list(lunile.keys()):
            return True
    else:
        return False


def zz(a,b):

    a = cnplist[5]
    b= cnplist[6]

def jj (a,b):
    a = cnplist[7]
    b = cnplist [8]
def nnn ():
    a = cnplist[9]
    b = cnplist[10]
    c = cnplist[11]
    d = ""
    if c == 0 and a>=1 or b>=1:
        return True
    elif c!=0:
        return True
    else:
        return False





def cc (a) :
    a = cnplist[12]

def cnp ():
    while True:

        #try:
            limita = 13
            #cnplist = []
            for i in range(0,limita):
                cnpq = int(input("Introdu cate o cifra urmat de tasta enter : "))
                cnplist.append(cnpq)
            print(f'Acesta este CNP ul introdus : {cnplist} !')


            if ss() is True:
                print(f"Indice sex: {ss()} !")
            else:
                print("Prima cifra este gresita, Va rugam incercati din nou !")
                return cnp()

            if ll() is True:
                print(f"Indice luna: {ll()} !")
            else:
                print(f"Indice luna: {ll()} !")
                print("Cifrele 4 si 5 sunt gresite, Va rugam incercati din nou !")
                return cnp()

            if nnn() is True:
                print(f"Indice NNN: {nnn()} !")
            else:
                print(f"Indice NNN: {nnn()} !")
                print("Cifrele 12, 11 si 10  sunt gresite, Va rugam incercati din nou !")
                return cnp()
            # q1 = input("da sau nu ?")
            # if q1 == "nu":
            #     continue
            # else:
            #     return cnpq


        # except:
        #         ValueError
        #         print("Cnp ul contine doar cifre ! Introdu de la capat ! ")
        #         continue
            break

cnp()
