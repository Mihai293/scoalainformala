# class MyFirstClass: #litere mari, daca avem mosteniri avem paranteze ()
#
#     pass
#
#
# my_first_object = MyFirstClass()

# class Caine:
#     nr_picioare = 4 #atribut
#
#     def __init__(self, name, age):#modul prin care construim instante de clasa #se aplica aceleasi reguli de parametri ca la functii
#         self.nume = name
#         self.varsta = age
#
#     def __str__(self):
#         return f"{self.nume} - {self.varsta}"
#
#     def change_name(self, name):
#         self.nume = name
#
# # print(Caine.nr_picioare)
#
# cainele_meu = Caine("Rex","2")
# # print(cainele_meu.nume)
# print(cainele_meu.change_name("Ben"))
# print(cainele_meu)

# class Calculator:
#
#     def __init__(self, op1, op2, operatie):
#         self.operator1 = op1 # self ne ajuta sa preluam valorile
#         self.operator2 = op2
#         self.operatie = operatie
#
#     def adunare(self):
#         return self.operator1 + self.operator2
#
#     def __str__(self):
#         if self.operatie == '+':
#             return f" {self.adunare()}"
#
# obiect1 = Calculator(1, 2, '+')
# print(obiect1)