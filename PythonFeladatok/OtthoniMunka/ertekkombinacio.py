def ValueCombination(numslist):
    value = []
    for i in range(len(numslist)):
        if numslist[i] >= 2000:
            value.append(numslist[i -2000])
        else:
            value.append(2000 - numslist[i])
    value.sort()
    print("A két legnagyobb elem: " + str(value[0]) + " " + str(value[1]))

#values = input("Adja meg a szamokat: ")
values = ( 21,30,21, 430, 810)
ValueCombination(values)

