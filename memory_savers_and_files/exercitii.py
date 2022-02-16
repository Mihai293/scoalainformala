# def func(*args):
#     return 3 + len(args)
#
# print(func (4, 4, 4))

# def exercitiu (i):
#     for i in range(i):
#         return i
# x = exercitiu(3)
# print(x)

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)

# x = [1, 2, 3, 4]
# print(x[-1:])


# a = [1, 2, 3]
# b = [4, 5]
# print(a + b *3)

# x = (1, 2, 3 )
# x[1] = 4

# x = [1,2,'hello','world',['another', 'list']]
# print(len(x[3]))


# x = 1
# def f ():
#     return x
# print(x)
# print(f())

# def functie(lista):
#     item = 1
#     for x, y in enumerate(lista):
#         item *= x
#         return lista[y + 1]
# lista = [ 1,2,3]
# print(functie(lista))

#List comprehension

# lista = []
# for item in 'Ana are mere':
#     lista.append(item)
# lista = [item for item in "ana are mere"]
# print(lista)

# my_numbers = [1,2,3,4,5]
# lista_numere = [item ** 2 for item in my_numbers if item % 2 ==0]
# print(lista_numere)

# lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x for x in lista_produse if "a"in x]
# print(lista_noua)

# lista = [x for x in range (10) if x<5]
# print(lista)

#Operator ternal
# a , b = 10, 20
# # min = a if a<b else b
# if a < b:
#     min = a
# else :
#     min = b
# print(min)

# lista_produse = ['ciocolata', 'suc', 'mere', 'miere', 'apa']
# lista_noua = [x if x != 'suc' else 'apaminerala 'for x in lista_produse]
# print(lista_noua)

#Functia filter
# lista_numere = [1,2,3,4,5,6,7,8,9,10]
# def funtie_nr_pare(number):
#     if number % 2 == 0:
#         return True
#     return False
# iterator_numere_pare = filter(funtie_nr_pare, lista_numere)
# print(list(iterator_numere_pare))
