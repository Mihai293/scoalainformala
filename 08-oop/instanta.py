class Rata:

    ochi = 2

    def __init__(self, inaltime, greutate, gen):
        self.inaltime = inaltime
        self.greutate = greutate
        self.gen = gen

    def merge(self): #metoda
        pass

    def macane(self):#metoda
        return "mac-mac"

rata_1 = Rata(inaltime=10, greutate=3.4, gen="F")#instantiere
rata_2 = Rata(inaltime=20, greutate=5, gen="M")

print(Rata.ochi)#acesare atribut de clasa
print(rata_1.macane())#pe baza unui obiect(rata_1)
