# print("Mesaj")
# format()
# a = input("X")
# def functia_mea(param_1):
#     pass

def suma (a, b, c=0) -> (int,str): #ordinea conteaza/daca parametrul b ii este alocata o valoare, toti trebuie sa fie alocati
#def suma (a: int, b:int = 1, c: int = 0) #parametri intrare
    """
    :param a:
    :param b:
    :param c:
    :return:
    """
    return a + b + c, a - b - c

variabila_1 = 1
variabila_2 = 2
# total = suma(variabila_1, variabila_2)
# total = suma(a=variabila_1, b= variabila_2) #corect si asa
# total = suma(variabila_1, b= variabila_2) #asa nu se poate, toti parametrii trebuiesc alocati la apelare
sum, dif = suma(a=variabila_1, b= variabila_2, c = 0) #parametreul c are valoare realocata
print(sum, dif)