def ValueCombination(numslist):
    value = []
    for i in range(len(numslist)):
        if int(numslist[i]) <= 2000:
            value.append(int(numslist[i]))
        else:
            value.append(int(numslist[i]) - 2000)
    value.sort()
    print("A két szám " + str(value[-1]) + " " + str(value[-2]))
    i = value[-1] + value[-2]
    print("A két szám összege: " + str(i))
    k = value[-1] * value[-2]
    print("A két szám szorzata: " + str(k))
    

#values = input("Adja meg a szamokat: ")
values = input("Kérek 5 számot:")
values.strip()
ValueCombination(tuple(values))

