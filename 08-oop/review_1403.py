# class ClasaMea:
#
#     gama = 0 #variabila de clasa
#
#     def __init__(self): #constructor
#         self.alpha = 1 # variabila de instance
#         self.__delta = 3 # variabila de instance privata
#
# obj = ClasaMea() #instantiere a clasei ClasaMew
# obj.beta = 2 #variabila de insntance si poate exista doar in interioru obj
# print(obj.__dict__) #dictionar care afiseaza obiectele clasei
# print(obj.alpha)#accesare self.alpha
# print(obj.gama)#accesare self.gama
# print(ClasaMea.gama)#accesare self.gama cu clasa
# print(obj._ClasaMea__delta) #afiseaza clasa privata cu denumirea luata din __dict__