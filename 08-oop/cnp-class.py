import datetime


class CNP:
    def __init__(self, cnp):
        self.cnp = cnp

    def data(self):
        try:
            z = ''.join([str(elem) for elem in self.cnp[1:7]])
            data_zi = datetime.datetime.strptime(z, "%y%m%d")
            return True
        except ValueError:
            return False

    def lungime(self):
        if len(self.cnp) != 13:
            return False
        else:
            return True


    def jj(self):
        a = self.cnp[7:9]
        judet_list = (
        '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18',
        '19', '20', '21', '22', '23', '24',
        '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', "41", '42',
        '43', '44', '45', '46',
        '51', '52')
        cod_judet = "".join(map(str, a))
        if cod_judet in list(judet_list):
            return True
        else:
            return False

    def nnn(self):
        a = self.cnp[9]
        b = self.cnp[10]
        c = self.cnp[11]

        if c == "0" and a >= "1" or b >= "1":
            return True
        elif c != "0":
            return True
        else:
            return False

    def alfanumeric(self):
        if self.cnp.isdigit():
            return True
        else:
            return False

    def control(self):
        cnpbst = int(self.cnp[-1])
        cast = '279146358279'
        rod = 0
        for x, y in enumerate(cast):
            rod += int(y) * int(self.cnp[x])
        intro = rod % 11
        if intro == 10:
            intro = 1
        else:
            intro = intro
        if cnpbst == intro:
            return True
        else:
            return False

    def sexcnp(self):
        i = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if self.sexcnp() in i:
            return True
        else:
            return False

    def __str__(self):
        if self.data() and self.lungime() and self.jj() and self.nnn() and self.alfanumeric() and self.control() is True:
            return "cnp Vaild"
        else:
            return "cnp Invalid"


if __name__ == "__main__":
    userInput = input("Introduceti cnp: ")
    inst = CNP(userInput)
    print(inst)
