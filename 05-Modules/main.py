# print() #rezulta str
# input() #rezulta str
# "".format() #str
# def functie2():
#     my_function()
#
# def my_function():
#     #function body - in corpul functiei trebuie sa avem return sau pass
#     return None #/or pass
#
# print(my_function())

# message()
#
# def message ():
#     print("enter a value")

# def your_function(name: str) -> str: #putem pune x in locul name si rezultatul va fi acelasi
#     print("hello", name)
#     return name
#
# name = input("numele meu este :")
# your_function(name)
#def my_function(a:str, b:str, c:str) ->(str, str, str):
    #return a, b, c

#print(my_function(a='1',c='2', b='3')) #scriere corecta chiar daca nu sunt in ordine
#print(my_function('1',c='2',b='3')) #corect
#print(my_function('3',a='1' ,c='2')) #incorect deoarece primul parametru trebuie sa fie a
#print(my_function('1','3', c='2')) #corect
#print(my_function('1','3', c='2' d='4'))# incorect pentru ca depasim numarul de parametri
#print(my_function('1','3'))#incorect, lipseste un parametru.#corect daca ii atribuim in declaratie o valoare

# def my_function():
#     pass
#
# a = my_function()
# print(a)
# b = None
# print(type(b))

# def my_function(n:int) -> bool :
#     if n % 2 == 0:
#         return True
#     return False #necesar
#
# print(my_function(3)) #returneaza None
# nr = input('Introdu un nr: ')
# if my_function(int(nr))is True:
#     print(("Nr este divizibil"))
# elif my_function(int(nr)) is False:
#     print("nr nu este vizibil")

# def my_function():
#     return f"Cunosti aceasta variabila: {var}"
# var=1 #name space global
# my_function()
# print(var)
try:
    valoare = int(input("prima cifra din cnp: "))
    #impartire = 1/valoare
    lista = [1]
    #lista.append ('2')
    #valoare = lista[0.5]
    print("sunt in try") #daca introduci string, nu se mai afiseaza acest print
except(TypeError, AttributeError, ValueError, ZeroDivisionError):
    print("tip de eroare")
else:
    print("nu exista exceptie")
finally:#se executa oricum
    print("se executa oricum")

#except Exception as e:
    #print("exceptie la impartire", e)