import string

def WordorNum(charrow):
    numcount = 0
    wordcount = 0
    upper = 0
    lower = 0
    magic = 0

    num = string.digits
    word = string.ascii_letters
    magicl = string.punctuation

    for i in charrow:
        if i in word:
            wordcount += 1
            if i.isupper() == True:
                upper += 1
            else:
                lower += 1
        elif i in num:
            numcount += 1
        elif i in magicl:
            magic += 1

    print("A karakter sorozatban " + str(numcount) + " szám " + str(lower) + " kisbetű " + str(upper) + " nagybetű és " + str(magic) + " írásjel találjató!")

row = input("Adj meg egy karakter sorozatot: ")
WordorNum(row)