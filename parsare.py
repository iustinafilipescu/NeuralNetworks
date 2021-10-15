import re


def coeficienti():
    file1 = open('ecuatii.txt', 'r')
    coef = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    rezultate = [0, 0, 0]

    for nr in range(0, 3):
        line = file1.readline()
        index = -1
        expr = re.split('\s', line)
        print(expr)
        for element in expr:
            index = index + 1
            if "x" in element:
                if len(element) == 1:  # este x simplu -> are coeficient 1
                    coef[nr][0] = 1
                else:
                    poz = element.find("x")
                    numar = element[0:poz]  # preluam coeficientul care e numarul lipit de x
                    if numar == "-":  # daca lipit de x este doar minus inseamna ca coef este -1
                        coef[nr][0] = -1
                    else:
                        coef[nr][0] = int(numar)  # transformam coeficientul in int din string
            if "y" in element:
                if index == 0:  # daca are index 0 inseamna ca x nu exista
                    if len(element) == 1:
                        coef[nr][
                            1] = 1  # si verificam ca mai sus la x daca primul element din expr este y singur inseamna ca are coef 1
                    else:
                        poz = element.find("y")
                        numar = element[
                                0:poz]  # daca nu, la fel preluam numarul lipit de y iar daca este minus inseamna ca e -1
                        if numar == "-":
                            coef[nr][1] = -1
                        else:
                            coef[nr][1] = int(numar)
                elif index != 0:  # daca exista x in expr va trebui sa verificam ce semn este dupa x
                    if expr[index - 1] == "+":  # elem de dinaintea celui cu y
                        if len(element) == 1:
                            coef[nr][1] = 1  # daca e plus si y e singur coef -> 1
                        else:
                            poz = element.find("y")
                            numar = element[0:poz]  # daca e plus iar y nu e singur preluam numarul lipit de y
                            coef[nr][1] = int(numar)
                    elif expr[index - 1] == "-":
                        if len(element) == 1:  # daca e minus in fata elem cu y si y e singur -> -1
                            coef[nr][1] = -1
                        else:
                            poz = element.find("y")  # la fel doar ca e cu minus
                            numar = "-" + element[0:poz]
                            coef[nr][1] = int(numar)
            if "z" in element:  # idem y
                if index == 0:
                    if len(element) == 1:
                        coef[nr][2] = 1
                    else:
                        poz = element.find("z")
                        numar = element[0:poz]
                        if numar == "-":
                            coef[nr][2] = -1
                        else:
                            coef[nr][2] = int(numar)
                elif index != 0:
                    if expr[index - 1] == "+":
                        if len(element) == 1:
                            coef[nr][2] = 1
                        else:
                            poz = element.find("z")
                            numar = element[0:poz]
                            coef[nr][2] = int(numar)
                    elif expr[index - 1] == "-":
                        if len(element) == 1:
                            coef[nr][2] = -1
                        else:
                            poz = element.find("y")
                            numar = "-" + element[0:poz]
                            coef[nr][2] = int(numar)
            if "=" in element:
                rezultat = int(expr[index + 1])
                rezultate[nr] = rezultat

    return coef,rezultate
