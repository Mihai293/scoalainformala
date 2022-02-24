import datetime
cnplist = []

def zz():
    try:
        z = ''.join([str(elem) for elem in cnplist[1:7]])
        data_zi = datetime.datetime.strptime(z, "%y%m%d")
        return True

    except ValueError:
        return False

def ss():

    a = cnplist[0]
    cnpdata = None
    sex1 = None
    start1 = datetime.datetime.strptime('01-01-1900', '%d-%m-%Y')
    end1 = datetime.datetime.strptime('31-12-1999', '%d-%m-%Y')
    start2 = datetime.datetime.strptime('01-01-1800', '%d-%m-%Y')
    end2 = datetime.datetime.strptime('31-12-1899', '%d-%m-%Y')
    start3 = datetime.datetime.strptime('01-01-2000', '%d-%m-%Y')
    end3 = datetime.datetime.strptime('31-12-2099', '%d-%m-%Y')
    if a == 1 or a == 2:
        if a == 1:
            sex1 = "M"

        else:
            sex1 = "F"
        cnpdata = cnplist[5], cnplist[6], cnplist[3], cnplist[4], 1, 9, cnplist[1], cnplist[2]
        cnp_data_fin = ''.join(map(str, cnpdata))
        data_cnp = datetime.datetime.strptime(cnp_data_fin, "%d%m%Y")
        if start1 <= data_cnp <= end1:
            return True
        else:
            return False

    elif a == 3 or a == 4:
        if a == 3:
            sex1 = "M"

        else:
            sex1 = "F"
        cnpdata1 = cnplist[5], cnplist[6], cnplist[3], cnplist[4], 1, 8, cnplist[1], cnplist[2]
        cnp_data_fin1 = ''.join(map(str, cnpdata1))
        data_cnp1 = datetime.datetime.strptime(cnp_data_fin1, "%d%m%Y")
        if start2 <= data_cnp1 <= end2:
            return True
        else:
            return False
    elif a == 5 or a == 6:
        if a == 5:
            sex1 = "M"

        else:
            sex1 = "F"
        cnpdata2 = cnplist[5], cnplist[6], cnplist[3], cnplist[4], 2, 0, cnplist[1], cnplist[2]
        cnp_data_fin2 = ''.join(map(str, cnpdata2))
        data_cnp2 = datetime.datetime.strptime(cnp_data_fin2, "%d%m%Y")
        if start3 <= data_cnp2 <= end3:
            return True
        else:
            return False
    elif a == 7 or a == 8 or a == 9:
        cnpdata3 = cnplist[5], cnplist[6], cnplist[3], cnplist[4], 1, 9, cnplist[1], cnplist[2]
        cnp_data_fin3 = ''.join(map(str, cnpdata3))
        data_cnp3 = datetime.datetime.strptime(cnp_data_fin3, "%d%m%Y")
        if start1 <= data_cnp3 <= end1:
            return True
        else:
            return False
    else:
        return False

def aa():
    g = cnplist[1:7]
    anul = ''.join(map(str, g))
    data_an = datetime.datetime.strptime(anul, "%y%m%d")

    start = datetime.datetime.strptime('01-01-1900', '%d-%m-%Y')
    end = datetime.datetime.strptime('19-03-2022', '%d-%m-%Y')

    if start <= data_an <= end:
        return True
    else:
        return False

def jj ():
    a = cnplist[7:9]
    judet_list = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24',
                  '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', "41", '42', '43', '44', '45', '46',
                  '51', '52')
    cod_judet = "".join(map(str, a))
    if cod_judet in list(judet_list):
        return True
    else:
        return False

def nnn ():
    a = cnplist[9]
    b = cnplist[10]
    c = cnplist[11]
    d = ""
    if c == 0 and a >= 1 or b >= 1:
        return True
    elif c != 0:
        return True
    else:
        return False

def cc () :
    a = cnplist[12]
    cnplist1 = cnplist[0:13]
    cifre = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]
    lista_inmultire1 = []

    for num1, num2 in zip(cnplist1, cifre):
        lista_inmultire1.append((num1 * num2))
    b = sum(lista_inmultire1)
    c = b % 11
    control = None
    if c == 10:
        control = 1
    else:
        control = c

    if control == a:
        return True
    else:
        return False

def cnp ():
    while True:

        try:
            limita = 13
            for i in range(0, limita):
                cnpq = int(input("Introdu cate o cifra urmat de tasta enter : "))
                cnplist.append(cnpq)
            print(f'Acesta este CNP ul introdus : {cnplist} !')

            if zz() is True:
                print(f"Indice zz: {zz()} !")

            else:
                print(f"Indice zz : {zz()} ! ")
                return cnp()


            if ss() is True:

                print(f"Indice sex: {ss()} !")

            else:
                print("Prima cifra este gresita, Va rugam incercati din nou !")
                return cnp()


            if nnn() is True:
                print(f"Indice NNN: {nnn()} !")
            else:
                print(f"Indice NNN: {nnn()} !")
                print("Cifrele 12, 11 si 10  sunt gresite, Va rugam incercati din nou !")
                return cnp()

            if aa() is True:
                print(f"Indice AA : {aa()} !")
            else:
                print(f"Indice AA: {aa()} !")
                print("Cifrele 6, 7 sunt gresite, Va rugam incercati din nou !")
                return cnp()

            if jj() is True:
                print(f"Indice JJ : {jj()} !")
            else:
                print(f"Indice JJ: {jj()} !")
                print("Cifrele 8, 9 sunt gresite, Va rugam incercati din nou !")
                return cnp()

            if cc() is True:
                print(f"Indice C : {cc()} !")
            else:
                print(f"Indice C : {cc()} !")
                print("Ultima cifra este gresita, Va rugam incercati din nou !")
                return cnp()

        except ValueError:
                print("Cnp ul contine doar cifre ! Introdu de la capat ! ")
                continue
        break

cnp()
