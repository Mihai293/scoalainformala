cnplist = [1,9,3,1,1,2,3,4,1,0,0,2]
cifre = [2,7,9,1,4,6,3,5,8,2,7,9]
lista_inmultire1 = []
# lista_inmultire = [cnplist[0] * cifre[0], cnplist[1] * cifre[1], cnplist[2] * cifre[2], cnplist[3] * cifre[3],
#                    cnplist[4] * cifre[4], cnplist[5] * cifre[5], cnplist[6] * cifre[6], cnplist[7] * cifre[7],
#                    cnplist[8] * cifre[8] ,cnplist[9] * cifre[9], cnplist[10] * cifre[10], cnplist[11] * cifre[11]]
for num1, num2 in zip (cnplist, cifre):
    lista_inmultire1.append((num1 * num2))

print(lista_inmultire1)
b = sum(lista_inmultire1)
print (b)
c = b % 11
control = None
if c == 10:
    control = 1
else:
    control == c
if control == cnplist[13]
    return True
else:
    return False


