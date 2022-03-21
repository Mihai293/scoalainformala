# #decorator=functie #comportament pe care doresti sa-l implementezi in fiecare functie
# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
# @decorator_simplu
# def functie_simpla ():
#     return"Buna seara ! "
#
# print(functie_simpla())

# def decorator_depozit(material):
#     def ambalaj(functia_noastra):
#         def amblaj_intern(*args):
#             print(f"Ambalam produse din {functia_noastra.__name__} cu {material}")
#             return f'{", ".join(x for x in functia_noastra(*args))}'
#         return amblaj_intern
#     return ambalaj
#
# @decorator_depozit("hartie")
# def impachetare_carti(*args):
#     return f"Impachetam carti: {args}"
#
#
# @decorator_depozit("folie_alimentara")
# def impachetare_fructe(*args):
#     return args
#
# print(impachetare_fructe("mere","pere"))
# # print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
#
#


# def decorator(functie):
#     def decoreaza(varf):
#         return functie(var)
#     return decoreaza
#
# def text (sir):
#     return sir.upper()
#
# text_p = decorator((text))
# print(text("Salut"))


# class Dog:
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property #ne ajuta sa folosim setter, deleter, getter
#     def name(self):
#         return self.__nume
#
#     @name.setter # ne ajuta sa redenumim
#     def name(self,nume):
#         self.__nume = nume
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
#
# my_dog = Dog(nume = "Rex")
# print(my_dog.name)
#
# my_dog.name = "Ben"
# print(my_dog.name)
#
# del my_dog.name
# print(my_dog.name)


# class Cat:
#     legs_no = 4
#
#     def __init__(self, nume):
#         self.__nume = nume
#
#     @property # getter
#     def name(self):
#         self.__nume = enumerate
#
#     @name.deleter
#     def name(self):
#         del self.__nume
#
#     def change_name(self, nume):
#         self.__nume = nume
#
#     def __str__(self):
#         return f"{self.__nume}"
#
# cat_object = Cat ("Fluffy")
# cat_object.change_name("Milly")
# print(cat_object)

# from datetime import date
#
# class Persoana:
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     @classmethod
#     def varsta_ani(cls, nume, varsta):#parametri dependenti de parametri din constructor
#         return cls(nume, date.today().year - varsta)
#
#     @staticmethod#nu este dependenta de constructor
#     def stare(ani):
#         return ani > 18
#
#
# persoana_1 = Persoana("Ion", 21)
# # print(persoana_1.varsta)
# persoana_2 = Persoana.varsta_ani("Maria", 20)
# print(persoana_2.varsta)
# print(Persoana.stare(22))