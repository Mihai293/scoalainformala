# 1. Vehicul
# 1.1 Vehicule de apa
# 1.2 Vehicul de aer
# 1.3 Vehicul de spatiu
# 1.4 Vehicul de terestru
# 1.4.1 Vehicul de teren
# 1.4.2 Vehicul de curs
# 1. este super clasa pentru 1.1 -> 1.4
# 1.1 -> 1.4 este subclasa pentru 1

#  2. Animale
# 2.1 Mamifere
# 2.1.1 Animale salbatice
# 2.1.2 Animale domestice
# 2.2. Reptile
# 2. pentru 2.1 si 2.2 sunt superclasa
# 2.1.1. si 2.1.2 pentru 2.1. sunt subclase
# 2.1.1. si 2.1.2 pentru 2 sunt subclase

# Max este un caine mare care doarme toata ziua.
# obiectul -> Max(substantiv)
# clasa -> caine(notiunea generica pe care se bazeaza)
# proprietatea -> mare (adjectiv)
# activitatea -> doarme (actiunea, verb) -> metode

# Un logan verde merge incet
# obiectul -> Logan
# clasa -> masina
# proprietatea -> verde
# activitatea -> merge incet

# Lenovo-ul gri se poate cumpara la un pret mai mic de pe un magazin online
#  obiectul -> Lenovo
#  clasa -> calculator
#  proprietatea -> gri/ se poate modifica in orice moment
#  activitatea -> se poate cumpara

#  Sa se realizeze jocul x si 0 intre doi jucatori in care :
#  primul jucator este mereu calculatorul
#  exista reguli de joc pentru mutari

# obiectul -> calculator/om
# clasa -> x si 0
# proprietatea -> primul jucator este mereu calc
# activitatea -> mutarile/ calculul de scor al jocului


# class MyFirstClass:
#     pass
#
# object = MyFirstClass()

# stack = []
#
# def push(val):
#     stack.append(val)
#     return stack
#
# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val
# print(push(3))
# print(push(2))
# print(push(1))
#
# print(pop())
# print(pop())
# print(pop())

# class Stack:
#     pass
#
#     def __init__(self):
#         self.__stack_list = [] #incapsulare
#
#     def push(self, val):
#         self.__stack_list.append(val)
#
#     def pop(self):
#         val = self.__stack_list[-1] #incapsulare
#         del self.__stack_list[-1]   #incapsulare
#         return val
#
#     def __str__(self):
#         return f"{self.__stack_list}"
#
# obiect_stiva = Stack()
# obiect_stiva.push(3)
# print(obiect_stiva)
# obiect_stiva.push(2)
# print(obiect_stiva)
# obiect_stiva.push(1)
# print(obiect_stiva)
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())
# print(obiect_stiva.pop())

# class ClasaExemplu():
#     def __init__(self, val= 1):
#         self.first = val
#         self.second = 0
#
#     def set_second (self, val= 2):
#         self.second = val
#
#     def __str__(self):
#         return f"{self.first} {self.second}"
#
# obiect_1 = ClasaExemplu()
# obiect_2 = ClasaExemplu(2)
#
# print(obiect_1)
# print(obiect_1.__dict__)
# print(obiect_2)
# print(obiect_3.second)


# class Caine:
#     nr_picioare = 4 #atribut
#
#     def __init__(self, name, age):#modul prin care construim instante de clasa #se aplica aceleasi reguli de parametri ca la functii
#         self.__nume = name
#         self.__varsta = age
#         self.cumpara = "spanac"
#         if self.__varsta == 4:
#             self.stare = "batran"
#         else:
#             self.cumapara = "jucarie"
#         #Caine.nr_picioare = 3
#
#
#     def __str__(self):
#         return f"{self.__nume} - {self.__varsta}"
#
#     def change_name(self, name):
#         self.__nume = name
#         return "ceva"
#
#
# obiect_1 = Caine ("rex", 4)
# print(type(obiect_1).__name__)
# print(obiect_1.__dict__)
# #var2 = obiect_1.__dict__
# print(obiect_1._Caine__nume)
# print(Caine.nr_picioare)
# print(Caine.__dict__)
# print(obiect_1.cumpara)
# print(hasattr(Caine, "nr_picioare")) # un fel de finder, afiseaza bolean