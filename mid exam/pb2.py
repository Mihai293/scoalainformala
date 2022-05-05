lista =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
def pb2(lista):
    while True:
        print(lista)
        lista.pop()
        lista.pop()
        lista.pop()

        if lista == [1]:
            return ("lista = []")
print(pb2(lista))
