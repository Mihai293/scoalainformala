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
#         #Caine.nr_picioare = 3 #reatribuirea var nr_picioare
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
# print(type(obiect_1).__name__) #sa ne dam seama din ce clasa provin
# print(obiect_1.__dict__) #afiseaza toate proprietatile
# #var2 = obiect_1.__dict__#scoatem o variabila in forma de dictionar
# print(obiect_1._Caine__nume)
# print(Caine.nr_picioare)
# print(Caine.__dict__)
# print(obiect_1.cumpara)
# print(hasattr(Caine, "nr_picioare")) # un fel de finder, afiseaza bolean

# class Star:
#
#     def __init__(self, nume, galaxie):
#         self.name = nume
#         self.galaxy = galaxie
#
#     def __str__(self):
#         return f"{self.name} este in {self.galaxy}"
#
# soare = Star("Soare", "Calea Lactee")
# print(soare)

# vehicul
# vehiculdeteren
# vehiculdetractare

# class Vehicul: #python permite mosteniri multiple. Vehicul tractare le poate vedea pe ambele
#     pass
#
# class VehiculTeren(Vehicul): #trecem in paranteze clasa pe care dorim sa o mosteneasca
#     pass
#
# class VehiculTractare(VehiculTeren):
#     pass

# parinti  sunt Vehicul pentru VehiculTeren si VehiculTractare(indirect)
# parinti sunt VehiculTeren pentru VehiculTractare
# parintii sunt super clase pentru copii(superclass)
# copii sunt VehiculTeren si VehiculTractare(indirect) pentru Vehicul
# copilul este vehiculTractare pentru vehiculTeren
# copii se numesc subclase
# print("Vehicul VehiculTeren VehiculTractare")
# for cls1 in [Vehicul, VehiculTeren, VehiculTractare]:
#     for cls2 in [Vehicul, VehiculTeren, VehiculTractare]:
#         print(issubclass(cls1, cls2), end='\t')
#     print()

# vehicul1 = Vehicul()
# vehicul_teren = VehiculTeren()
# vehicul_tractare = VehiculTractare()
# print(isinstance(vehicul_teren, Vehicul)) #asa vedem daca clasa are o mostenire(daca vehicul_teren il mosteneste pe Vehicul)

#Interviu #is verifica daca se pointeaza catre acel obiect si egal-egal verifica valoarea

# class Exemplu:
#     def __init__(self,val):
#         self.value = val
#
# obiect_1 = Exemplu(0)
# obiect_2 = Exemplu(2)
# obiect_3 = obiect_1
# obiect_3.value += 1
#
# print(obiect_1 is obiect_2)
# print(obiect_2 is obiect_3)
# print(obiect_3 is obiect_1)
# print(obiect_1.value, obiect_2.value, obiect_3.value)

# string_1 = "Maria are mere "
# string_2 = "Maria are mere mari"
# string_1 += "mari"
# print((string_1 == string_2, string_1 is string_2))

# class SuperClass:
#
#     supVar = 1
#
#     def __init__(self, nume):
#         self.name = nume
#
#     def __str__(self):
#         return f"Numele meu este {self.name}"
#
# class Clasa3:
#
#     variabila_clasa = 5
#
#     def __init__(self,name):
#         self.name = name
#
# class SubClass(Clasa3, SuperClass):
#
#     subVar = 2
#
#
#     def __init__(self,nume):
#         #Super.__init__(self,nume)
#         super().__init__(nume) #aceiasi metoda ca cea de sus
#
#     def __str__(self):
#         return f"Nume"
#
# obiect = SubClass("Alexandra")
# print(obiect.subVar)
# print(obiect.supVar)


class A:

    def info(self):
        return "Clasa A"

class B(A):
    pass
    # def info(self):
    #     return "Clasa B"

class F:
    def info(self):
        return "Clasa F"

class C(A):
    pass
    # def info(self):
    #     return "Clasa C"

class D(A, C):
    pass

print(D().info()) # va returna clasa B pentru ca se incepe cu prima din STANGA
print(D().info()) # va returna clasa C pentru ca se incepe cu prima din STANGA iar in B nu se afla nimic
print(D().info()) # va returna clasa C pentru ca se incepe cu prima din STANGA iar in B nu se afla nimic
print(D().info()) # va returna clasa A pentru ca nu gaseste nimic si pleaca pe super clasa primei de la stanga, adica B
#error MRO - eroare ordine mostenire
#nu se permite mostenirea inlantuita