#1

"""
. Feladat
Írj eljárást, amely egy tetszőleges szöveget, ill. alakzatot ír ki a képernyőre!
"""

"""
def kiir():
    print("szeretlek")
kiir()
"""

#------------------------------------------------

#2
"""
. Feladat
Írj eljárást, amely paraméterül kapott számról eldönti, és a képernyőre kiírja, hogy negatív, pozitív vagy nulla-e!
"""

"""
def pvagyn(x):
    if x > 0:
        return print(f"A {x} szám pozitiv.")
    if x < 0:
        return print(f"A {x} szám negativ.")
    if x == 0:
        return print(f"A {x} szám egyenlő 0-val.")
pvagyn(0)
"""

#---------------------------------------------------------------

#3
"""
3. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám! Kezeld azt az esetet is, ha a két szám egyenlő!
"""

"""
def szamok(x, y):
    if x > y:
        return print(f"A {x} nagyobb mint a {y}.")
    if x < y:
        return print(f"A {x} kisebb mint a {y}.")
    if x == y:
        return print(f"A {x} és a {y} egyenlő.")
szamok(5, 6)
"""

#------------------------------------------------------------------

#4.
"""
4. Feladat
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!

"""
"""
lista= []

for i in range(3):
    nev = input("Kérek egy nevet: ")
    lista.append(nev)
def legrovidebb():
    kicsi = lista[0]
    for i in lista:
        if len(i) > len(kicsi):
            i = kicsi
    return print(f"A legrövidebb szó: {i}")

legrovidebb()
"""

#---------------------------------------------------------------

#5.

"""
5.1 Feladat
A "Próbáld ki!" gombra kattintva elérhető egy program, ami egy eljárás segítségével kirajzol a képernyőre egy 6x3-as mezőt. Alakítsd át ezt a programot úgy, az eljárás hívásakor megadott értékpárnak megfelelően a program az adott pozícióba 'O' helyett '+' jelet írjon ki. A lenti példában az eljárás hivása: mezot_rajzol(0,4)
"""
def mezot_rajzol(szel, hossz):
    szel -= 1
    hossz -= 1
    for sor in range(3):
        for oszlop in range(6):
            if oszlop == szel and hossz == sor:
                print('+ ', end='')
                szel +=10
            else:
                print('O ', end='')
        print()

mezot_rajzol(4,2)