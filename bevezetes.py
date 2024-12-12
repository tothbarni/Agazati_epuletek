def jatekos():
    nev:str = input("Játékos neve: ")
    szerep:str = input("szerepkör: ")
    hp:int = 8
    if (szerep.lower() == "varázsló"):
        hp = 2
    elif (szerep.lower() == "harcos"):
        hp = 10
    print(f"Üdvözlünk {nev}, {hp} életed van!")