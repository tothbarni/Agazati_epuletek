import random
def fej_iras():
    dobasok = []
    for i in range(0, 7, 1):
        rnd_dob = int(random.random() * 2)
        if (rnd_dob == 0):
            dobasok.append("ÍRÁS")
        else:
            dobasok.append("FEJ")
    
    eredmeny = ""
    for i in range(0, len(dobasok)-1):
        if (i > 0):
            eredmeny += "-"
        eredmeny += dobasok[i]
    print(eredmeny)
    return dobasok

def fejek_szama(dobasok):
    db:int = 0
    for i in range(0, len(dobasok)):
        if (dobasok[i] == "FEJ"):
            db += 1
    return db

def konzol_kiir(szoveg:str, db:int):
    print(f"{szoveg} {db}")

def file_kiir(db):
    f = open("fejek.txt", "a")
    f.write("II/F:\n")
    f.write(f"A fejek száma: {db}")
    f.close()