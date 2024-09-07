nums = input("Add meg a számokat: ")

result = tuple(nums)

def Main(nums):


    numlist = []
    paros=0
    paratlan=0

    for i in nums:
        if i != ",":
            numlist.append(int(i))


    for k in numlist:
        if k%2 != 0:
            paratlan+=1
        else:
            paros+=1

    print("Paros szamok száma " + str(paros))
    print("Páratlan számok száma " + str(paratlan))

Main(nums)