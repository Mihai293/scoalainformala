lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def pb2(lista):
    while True:
        lista.pop()
        print(lista)
        if lista == []:
            return ("lista = []")
print(pb2(lista))
