#Problema 1

# class Catalog:
#
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#         self.absente = 0
#         self.materii = {}
#
#     def __str__(self):
#         return f"{self.nume} {self.prenume} \n \t materii si note:{self.materii} \n \t absente: {self.absente}"
#
#     def increment_abs(self):
#         self.absente +=1
#
#     def delete_abs(self, numar_abs):
#         if self.absente > 0:
#             self.absente -= numar_abs
#
#
# class Extensie1(Catalog):
#     def __init__(self,nume, prenume):
#         super().__init__(nume, prenume)
#
#     def add_subject(self, materie, note):
#         self.materii.update({materie:note})
#         self.note = note
#
#     def print_all(self):
#         return f"{self.materii.keys()}"
#
#     def final_grade(self):
#
#         note_finale = {}
#
#         for i, j in self.materii.items():
#             if self.note.isdigit():
#                 if all(isinstance(x, int) for x in j):
#                     medie = sum(j) / len(j)
#                     note_finale.update({i: medie})
#         return note_finale
#
#
#
#
#
# student = Catalog("Roata", "Ion")
# print(student)
# student.increment_abs()
# student.increment_abs()
# student.increment_abs()
# print(student)
# student.delete_abs(2)
# print(student)
#
# student2 = Catalog("Cerc", "George")
# print(student2)
# student2.increment_abs()
# student2.increment_abs()
# student2.increment_abs()
# student2.increment_abs()
# print(student2)
# student2.delete_abs(2)
# print(student2)
#
# obj = Extensie1("Ana", "Maria")
# obj.add_subject("Python", [5, 7, 9])
# obj.add_subject("Java", [4, 5, 9])
# print(obj.final_grade())

#Problema 2
#
# from operator import itemgetter
#
#
# class CatalogPrajituri:
#
#     lista_prajituri = []
#
#     def __init__(self, nume, pret, gramaj):
#         self.nume = nume
#         self.pret = pret
#         self.gramaj = gramaj
#         prajituri = [self.nume, self.pret, self.gramaj]
#         self.lista_prajituri.append(prajituri)
#
#     @staticmethod
#     def sortare_gramaj():
#         prajituri_gramaj = sorted(CatalogPrajituri.lista_prajituri, key=itemgetter(2))
#         return f"Prajiturile in functie de pret sunt {prajituri_gramaj}"
#
#     @staticmethod
#     def sortare_pret():
#         prajituri_pret = sorted(CatalogPrajituri.lista_prajituri, key=itemgetter(1))
#         return f"Prajiturile in functie de pret sunt {prajituri_pret}"
#
#     def __str__(self):
#         return f"Prajitura {self.nume} avand pretul {self.pret} lei, cu un gramaj de {self.gramaj} grame."
#
#
# class Tort(CatalogPrajituri):
#
#     def __init__(self, nume, pret, gramaj, etajat = False, glazura = "ciocolata"):
#         super().__init__(nume, pret, gramaj)
#         self.etajat = etajat
#         self.glazura = glazura
#
#     def __str__(self):
#         return f"Tortul {self.nume} are o glazura de {self.glazura} fiind etajat {self.etajat}, avand un pret de {self.pret} lei si un gramaj de {self.gramaj} grame."
#
#
# class Fursec(CatalogPrajituri):
#
#     def __init__(self, nume, pret, gramaj):
#         super().__init__(nume, pret, gramaj)
#
#     def __str__(self):
#         return f"Fursecul {self.nume}, avand un pret de {self.pret} lei si un gramaj de {self.gramaj} grame."
#
#
# prajitura1 = CatalogPrajituri("Eclere", 10, 300)
# prajitura2 = CatalogPrajituri("Lava Cake", 21, 150)
# prajitura3 = CatalogPrajituri("Tiramisu", 35, 750)
#
# tort1 = Tort("Black Forest", 82, 1150, etajat=True, glazura="cacao")
# tort2 = Tort("Oreo", 91, 950, etajat=False, glazura="Nutella")
# tort3 = Tort("Apple Caramel", 67, 1250, etajat=False, glazura="Caramel")
#
# fursec1 = Fursec("Vanilla Cookie", 12, 100)
# fursec2 = Fursec("Oat Cookie", 31, 450)
# fursec3 = Fursec("Chocolate Cookie", 25, 350)
#
# print(prajitura1)
# print(prajitura2)
# print(prajitura3)
# print(tort1)
# print(tort2)
# print(tort3)
# print(fursec1)
# print(fursec2)
# print(fursec3)
# print("\n")
# print(CatalogPrajituri.sortare_pret())
# print("\n")
# print(CatalogPrajituri.sortare_gramaj())


#Problema 3

# class CatalogAuto:
#     def __init__(self, marca, tip):
#         self.marca = marca
#         self.tip = tip
#
#     def schimbare_culoare(self, culoare):
#         self.culoare = culoare
#
#     def __str__(self):
#         return f"Culoarea este: {self.culoare()}"
#
# class ScauneIncalzite(CatalogAuto):
#     def __init__(self, scaune_incalzite ,marca, tip):
#         super().__init__(marca, tip)
#         self.scaune_incalzite = scaune_incalzite
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, Tipul este: {self.tip}\n\t, Culoarea este{self.scaune_incalzite}"
#
# class BlocuriOpticeLed(CatalogAuto):
#     def __init__(self, blocuri_optice_led, marca, tip):
#         super().__init__(marca, tip)
#         self.blocuri_optice_led = blocuri_optice_led
#
#     def __str__(self):
#         return f"Marca este: {self.marca}, Tipul este: {self.tip}\n\t, Blocuri optice{self.blocuri_optice_led}"
#
# obj = ScauneIncalzite(marca = "Aro", tip = 461, scaune_incalzite = "NU")
# # print(obj)
# # obj.schimbare_culoare("rosu")
# # print(obj.culoare)
#
# obj2 = BlocuriOpticeLed(marca = "Dacia", tip = 1310, blocuri_optice_led="NU")
# print(obj2)
# obj2.schimbare_culoare("negru")
# print(obj2.culoare)
# print(obj2.culoare, obj2.blocuri_optice_led, obj2.marca, obj2.tip)
# print(obj.scaune_incalzite, obj.tip, obj.marca)

#Problema 4

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
