# class Mate:
#     def __init__(self,a=1, b=2, c=3, d=4):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def verificare(self):
#         self.e = "Informatiile nu sunt corecte"
#         if str(self.a).isnumeric() and str(self.b).isnumeric() and str(self.c).isnumeric():
#             self.e = (self.a*(self.b + 3)/self.c)*self.d
#         return self.e
#
#     def __str__(self):
#         return f'Rezultatul este: {self.verificare()}'

# obiect = Mate()
# print(obiect)
# obiect2= Mate(2,3,4,5)
# print(obiect2)
# obiect3 = Mate('x', 'y', 'z', 4)
# print(obiect3)
# obiect4 = Mate(9,2)
# print(obiect4)



# Creati 3 clase ce vor reprezenta un catalog auto:
# • Clasa1 • La initializare trebuie sa oferim doi parametrii de intrare marca si tip • Are o
# metoda ce accepta parametrul de intrare culoare. De asemenea o metoda numita
# AfisareCuloare pentru afisarea culorii. Folositi metoda pentru afisare.
# • Clasa2 : • Mosteneste Clasa1 si avem o metoda care adauga argumentul scaune_incalzite
# ca parametru de intrare
# • Clasa3 : • Mosteneste Clasa1 si avem o metoda care adauga argumentul
# Blocuri_Optice_LED ca parametru de intrare
# • Creati un obiect al Clasei 2 (marca = ARO,Tip = M461) si folositi metoda de creare argum
# DA. scaune_incalzite cu valoarea Nu;
# Creati argumentul culoare cu valoarea rosu
# • Creati un obiect al Clasei 3 (marca = Dacia, Tip = 1310) si folositi metoda de creare argum.
# Blocuri_Optice_LED cu valoarea Nu; Creati argumentul culoare cu valoarea negru
# • Afisati pe rand argumentele culoare, Blocuri_Optice_LED, scaune_incalzite marca si tip a
# obiectelor create

# class Masina:
#     def __init__(self, marca, tip):#constructor
#         self.marca = marca #variabila de instanta(__marca -> privata)
#         self.tip = tip
#
#     def schimbare_culoare(self, culoare): #metoda
#         self.culoare = culoare
#
#     def __str__(self): #afisare
#         return f'Afisare culoare {self.culoare}'
#
# class Optiuni(Masina):
#
#     def __init__(self, scaune_incalzite, marca, tip):
#         super().__init__(marca, tip)
#         self.scaune_incalzite = scaune_incalzite
#
#     def __str__(self):
#         return f" Marca este {self.marca} si tipul este {self.tip} cu scaune incalzite: {self.scaune_incalzite}"
#
# class Extra_Optiuni(Masina):
#     def __init__(self, blocuri_optice_led, marca, tip):
#         super().__init__(marca, tip)
#         self.blocuri_optice_led = blocuri_optice_led
#
#     def __str__(self):
#         return f"Marca este {self.marca} si tipul este {self.tip} cu blocuri lumini: {self.blocuri_optice_led}"
#
# obj = Optiuni(marca='aro', tip="M461", scaune_incalzite='NU') #obiect
# # print(obj) #printare obiect
# #
# # obj.schimbare_culoare("rosu") #apelare medota si modificare parametru
# # print(obj.culoare) #afisare parametru
#
# # • Creati un obiect al Clasei 3 (marca = Dacia, Tip = 1310) si folositi metoda de creare argum.
# # Blocuri_Optice_LED cu valoarea Nu; Creati argumentul culoare cu valoarea negru
# # • Afisati pe rand argumentele culoare, Blocuri_Optice_LED, scaune_incalzite marca si tip a
# # obiectelor create
#
# obj3 = Extra_Optiuni(marca="Dacia", tip= "1310", blocuri_optice_led="NU")
# print(obj3)
# obj3.schimbare_culoare("negru")
# print(obj3.culoare)
# print(obj3.blocuri_optice_led)
# print(obj.scaune_incalzite)
# print(obj.marca)
# print(obj.tip)

# class Dog:
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property
#     def name(self):
#         return self.__nume
#
# my_dog = Dog(nume="Rex")
# print(my_dog.name)


# Creati o clasa care se numeste lista_CD_DVD.
# La crearea unui obiect ala cestei clase va solicita doua argumente reprezentand titlu si
# continut cu care va crea doua atribute.
# Fiecare obiect creat va fi adaugat intr-o lista din namespace-ul global Clasa are o
# metoda care cauta si gaseste pe baza textului dat ca argument un obiect, afisiand titlu
# si continutul. Se va folosi lista de obiecte pentru a cauta.
# La afisarea obiectului returnati utilizand metoda __str__ titlul obiectului.
# Aplicati clasa pentru 3 exemple apoi folositi cautarea pe un caz pozitiv si unul
# negativ. Printati cele 3 obiecte.

class Lista_CD_DVD:

    lista = []

    def __init__(self, titlu, continut):
        global lista
        self.titlu = titlu
        self.continut = continut
        obiecte = [self.titlu, self.continut]
        self.lista.append(obiecte)


    @staticmethod
    def cautare(argument):
        msj = "ERR"
        for i in Lista_CD_DVD.lista:
            if argument in i[0] or argument in i[1]:
                msj = f"Obiectivul cautat este Titlul : {i[0]} Continut: {i[1]}"
                return msj
        return msj

    def __str__(self):
        return f"{self.titlu}"

obj = Lista_CD_DVD("Castravete","Culinar")
obj1 = Lista_CD_DVD("Fotbal","Sport")
obj2 = Lista_CD_DVD("Cs","Game")

print(Lista_CD_DVD.cautare("Castravete"))
print(Lista_CD_DVD.cautare("fifi"))
print(Lista_CD_DVD.cautare("cs"))