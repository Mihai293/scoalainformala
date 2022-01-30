#tupluri
lista = [1,2,3,1,'a']
lista_1 = ['a','b','c']
lista_total = lista + lista_1
# print(lista_total)
# tuplu =(1,2,3,1,'a')
# tuplu_1 = (1,2,3,'b')
# tuplu_total = tuplu + tuplu_1
# print(tuplu_total)
#tuplu_nou = (1,) # tuplu cu un singur element are nevoie de virgula la final pentru a fi clasificat ca tuplu
#print(type(tuplu_nou)) #exemplu(class tuple)

dictionar = {"cheie1" : '1', 1: '1' , 'lista':[1,2,3]}
print(dictionar['cheie1'])
#print(dictionar.get('cheie1')) #o alta modalitate de print
#dictionar['cheie1'] = 2#schimbare valoare pt cheie1
#dictionar['cheie2'] = 3 #adaugare cheie 2 la sf dictionar
#dictionar.update({'cheie1':2}) #schimbare valoare pt cheie1
#dictionar.update({'cheie2':4}) #daca cheia nu exista se va adauga
#dictionar.update({'cheie1':2}) #daca cheia nu exista se va adauga
#print(dictionar)
#print(dictionar.keys())
#print(dictionar.values())
#print(dictionar.items()) #organizare sub forma de tuplu

#seturi
# setul_meu = {1,1,3}
# print(setul_meu) #afiseaza doar elemente unice
# print(lista_total)
#print(set(lista_total)) #convertirea listei la set, afisand doar elementele unice