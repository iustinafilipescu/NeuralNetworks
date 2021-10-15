import parsare

if __name__ == '__main__':
    A, B = parsare.coeficienti()


def determinantul(matrice):  # metoda cand scrii primele 2 linii sub matrice
    if len(matrice) == 2:  # cand matricea e 2x2 - pt determinantul minorilor
        det = matrice[0][0] * matrice[1][1] - matrice[0][1] * matrice[1][0]
    elif len(matrice) == 3:  # cand matricea e 3x3
        det = matrice[0][0] * matrice[1][1] * matrice[2][2] + matrice[1][0] * matrice[2][1] * matrice[0][2] + \
              matrice[2][0] * matrice[0][1] * matrice[1][2] - matrice[0][2] * matrice[1][1] * matrice[2][0] - \
              matrice[1][2] * matrice[2][1] * matrice[0][0] - matrice[2][2] * matrice[0][1] * matrice[1][0]
    if det == 0:
        return False
    return det


def minori(matrice, i, j):  # minorul elementului de pe poz i,j din matrice
    return [linia[:j] + linia[j + 1:] for linia in (matrice[:i] + matrice[i + 1:])]
    # returneaza din fiecare linie elementele fara cel de pe poz j (eliminand coloana)  din  liniile fara linia i (eliminand linia) din matrice


def matriceMinori(matrice):
    mMinori = []
    for i in range(len(matrice)):
        rand = []
        for j in range(len(matrice)):
            rand.append(determinantul(
                minori(matrice, i, j)))  # calculam det fiecarui minor in parte si in punem in matricea de minori
        mMinori.append(rand)
    # schimbam semnul unde suma indicilor e impara (inmultirea cu -1)
    mMinori[0][1] = -mMinori[0][1]
    mMinori[1][0] = -mMinori[1][0]
    mMinori[1][2] = -mMinori[1][2]
    mMinori[2][1] = -mMinori[2][1]
    return mMinori


def transpusa(matrice):  # prima coloana devine prima linie s.a.m.d
    transpusa = [[matrice[0][0], matrice[1][0], matrice[2][0]], [matrice[0][1], matrice[1][1], matrice[2][1]],
                 [matrice[0][2], matrice[1][2], matrice[2][2]]]
    return transpusa;


def inversa(matrice, det):  #impart fiecare element la determinant

    for i in range(len(matrice)):
        for j in range(len(matrice)):
            matrice[i][j] = matrice[i][j] / det
    return matrice


adjoint=transpusa(matriceMinori(A))
if determinantul(A) == 0:
    print("nu exista solutie")
inversaA=inversa(adjoint,determinantul(A))

solutie = [0, 0, 0]

#produs scalar
for i in range(len(inversaA)):
    for j in range(len(B)):
        solutie[i] += inversaA[i][j] * B[j]

print(solutie)


