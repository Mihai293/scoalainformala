#Reguli
#daca primul caracter si ultimul se repetau in cuvant, caracterul trebuia afisat
#restul caracterelor erau ascunse
#7sanse de castig
#word = 0 _ 0 _ _ _ _ o _ee
word = "onomataopee"
#litera_cuvant = input(" Alege o litera")
#print(litera_cuvant)
lista_cuvant = []
for iterator in word:
    lista_cuvant.append("_")
    if iterator == word[0] or iterator == word[-1]:
        lista_cuvant[-1] = iterator
print("".join(lista_cuvant))
numar_incercari = 1
lista_litere_incercate = set()
while numar_incercari <= 7 :
    litera = input("Alege o litera :").lower()
    if litera in word :
        for index, valoare in enumerate(word):
            if valoare == litera:
                lista_cuvant[index] = litera
    else :
        if litera not in lista_litere_incercate :
            numar_incercari +=1
        lista_litere_incercate.add(litera)
        print(f'Litera nu exista, deja ai incercat urmatoarele litere: {",".join(lista_litere_incercate)}')
        print(f"Mai ai {7-numar_incercari} incercari !")

    if 8 - int(numar_incercari)==0:
        print(f"Ai pierdut ! Cuvantul era {word}")
    elif ''.join(lista_cuvant)==word :
        print("Ai castigat !")
        break
    else :
        print(" ".join(lista_cuvant))
