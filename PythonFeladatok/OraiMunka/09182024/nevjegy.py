nevjegyek = []


while True:
    nev = input("Add meg a neved (bezar a befejezeshez): ")
    nev = nev.strip()

    if nev == "bezar" or nev == "bezár":
        break

    telefon = input(f"Add meg a {nev} telefonszamat: ")
    nevjegyek.append(f"{nev} , {telefon}")

with open("nevjegyek.txt", "w", encoding="utf-8") as f:
    for nevjegy in nevjegyek:
        f.write(nevjegy)






