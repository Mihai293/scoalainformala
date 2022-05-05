# Problema 1

# class Calcul:
#     def __init__(self, a=1, b=2, c=3, d=4 ):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.d = d
#
#     def verificare(self):
#         self.e = f"Informatiile introduse nu sunt cifre"
#         if str(self.a).isnumeric() and str(self.b).isnumeric()and str(self.c).isnumeric() and str(self.d).isnumeric():
#             self.e = (self.a * (self.b + 3) / self.c) * self.d
#         return self.e
#
#     def __str__(self):
#         return f"Rezultatul este: {self.verificare()}"
#
# obiect = Calcul()
# print(obiect)
# obiect2=Calcul(5,6,7,8)
# print(obiect2)
# obiect3 = Calcul("x","y","z",2)
# print(obiect3)
# obiect4 = Calcul(9,2)
# print(obiect4)

# Problema 2

# class Lista_CD_DVD:
#
#     lista = []
#
#     def __init__(self, titlu, continut):
#         global lista
#         self.titlu = titlu
#         self.continut = continut
#         obiecte = [self.titlu, self.continut]
#         self.lista.append(obiecte)
#
#
#     @staticmethod
#     def cautare(argument):
#         msj = "ERR"
#         for i in Lista_CD_DVD.lista:
#             if argument in i[0] or argument in i[1]:
#                 msj = f"Obiectivul cautat este Titlul : {i[0]} Continut: {i[1]}"
#                 return msj
#         return msj
#
#     def __str__(self):
#         return f"{self.titlu}"
#
# obj = Lista_CD_DVD("Castravete","Culinar")
# obj1 = Lista_CD_DVD("Fotbal","Sport")
# obj2 = Lista_CD_DVD("Cs","Game")
#
# print(Lista_CD_DVD.cautare("Castravete"))
# print(Lista_CD_DVD.cautare("fifi"))
# print(Lista_CD_DVD.cautare("cs"))


# class Util:
#     lista = []
#
#     def __init__(self,continut):
#         self.continut = continut
#         obiect = [self.continut]
#         self.lista.append(obiect)
#
# class Izatori:
#     def __init__(self, user, parola):
#         self.user = user
#         self.parola = parola
#
# class Utilizatori(Izatori, Util):
#     def parole:
#         return self.parola
