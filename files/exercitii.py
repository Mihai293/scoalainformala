#  Realizati o functie care sa inlocuiasca textul din variabila string aflat
# intre valorile “start” si “end” cu textul din “text”.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be
# introduced."
# # [start, end, text]
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
# Textual rezultat este: The Conquistator must meet King on top of Palace
# battlements to be introduced.
# Numaratoarea de start si end incepe cu indexul 1. Se pot introduce de la
# tastatura alte valori pentru index si text, cat si un numar mai mare de liste.
# Optimizati codul.
# string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# # [start, end, text]
# patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]

# def nameChanger(x, y, z):
#     string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
#     # 42 -> 49
#     # string = "The Inquisitor must meet Varric on top of Palace's battlements to be introduced."
#     # 25 -> 31
#     # string = "The Inquisitor must meet King on top of Palace's battlements to be introduced."
#
#     start = string[5:14]
#     end = string[26:31]
#     text = string[43:49]
#     string2 = string.replace(start, x)
#     string3 = string2.replace(end, y)
#     string4 = string3.replace(text, z)
#     #print(string4)
# string_value = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."
# lista = [[5, 14, 'Conquistador'],[26,31,'King'],[43,49,'Palace']]
# for i in sorted(lista, reverse=True):
#     #print(i, string_value[i[0]-1:i[1]])
#     string_value = string_value.replace(string_value[i[0]-1:i[1]], i[2])
#     print(string_value, '>>>')
#
# nameChanger("Conquistador", "King", "Palace")





# Se da urmatoarea lista:
# lista_nume = ['Maria','Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']
# # Se cere:
# # 1. Sortati lista dupa nume
# # 2. Determinati numarul de aparitii al fiecarui nume
# # 3. Listati numele care apare de cele mai multe ori in lista initiala.
# # 4. Listati numele care apare de cele mai putine ori in lista initiala.
# lista_nume.sort()
# print(lista_nume)
# print((lista_nume.count(0))
# for x in sorted(lista_nume, key=lambda x: x.split(",")[0]):
#     print x



#Grile
# num_calls = 0
#
# def exe (x):
#     global num_calls
#     num_calls = 3
#     num_calls += 1
#     return x * x
# print(exe(4))

# x = 1
#
# def f():
#     return x
# print(x)
# print(f())

# x = [1, 2, "hello", "world", ["another","list"]]
# print(len(x[4][0]))

# x = (1, 2, 3)
# x[1] = 4

# x = [1, 2, 3, 4,5,6,7,8,9]
# y = x[-1:]
# print(y)

# x = [0, 1, [2]]
# x[2][0] = 3
# x[2].append(4)
# x[2] = 2
# print(x)


# a = range(10)
# y = [x*x for x in a if x%2 == 0]
# print(y)

# def make_acount():
#     return {'balance': 0}
#
# def deposit(acount, amount):
#     acount["balance"] += amount
#     return acount['balance']
#
# a = make_acount()
# print(deposit(a,10))

# class BankAcount:
#     def __init__(self):
#         self.balance = 0
#     def deposit(self,amount):
#         self.balance += amount
#         return self.balance
# a = BankAcount()
# b = BankAcount()
# print(a.deposit(100))

# "foo" + 2

# try:
#     print("a")
# except:
#     print("b")
# else:
#     print("c")
# finally:
#     print("d")

# for k in {'x':1, 'y':2}:
#     print(k)

# print(list("python"))

# def func (*args):
#     return 3 + len(args)
# print(func(4, 4, 4))

# count = (3, 2, 5, 4)
# while len(count) < 5:
#     count0 = count[0]+1
#     print("hello")

# def exercitiu(var):
#     for letter in 'geeksforgeeks':
#         if letter == 'e' or letter  == "s":
#             continue
#         print("current letter: ",letter)
#         var = 10
#         return var
# print(exercitiu(20))

# def f(a, list = []):
#     for i in range (a):
#         list.append(i*i)
#     print(list)
# f(3)
# f(2,[1, 2, 3])
# f(2)

# list = ['1', '2', '3', '4', '5']
# print (list[12:])