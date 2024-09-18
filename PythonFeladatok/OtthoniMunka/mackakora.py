macskaev = input("Hány éves a macska: ")


def Catcalc(age):
    incattime = 0

    if age <= 2:
        for i in range(age):
            incattime+=10.5

    else:
        incattime+=21
        for i in range(age-2):
            incattime+=4

    print(round(incattime))


Catcalc(int(macskaev))





