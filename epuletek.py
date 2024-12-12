from Epulet import Epulet

def beolvas(fajlnev="epulet.txt"):
    epuletek = []
    fajlom = open(fajlnev, "r", encoding="UTF-8")
    next(fajlom)
    tobbi_sor = fajlom.readlines()
    
    i = 0
    while i < len(tobbi_sor):
        sor_lista = tobbi_sor[i].strip().split("$")
        epuletek.append(Epulet(*sor_lista))
        i += 1

    fajlom.close()
    return epuletek

def epuletek_szama(epuletek):
    return len(epuletek)

def magas_epuletek_szama(epuletek):
    lab_mertek = 555 / 3.280839895
    szamlalo = 0
    i = 0
    szamlalo = 0
    while i < len(epuletek):
        if epuletek[i].magassag > lab_mertek:
            szamlalo += 1
        i += 1
    return szamlalo

def legoregebb_epulet_orszaga(epuletek):
    legoregebb = epuletek[0]
    i = 1
    while i < len(epuletek):
        if epuletek[i].ev < legoregebb.ev:
            legoregebb = epuletek[i]
        i += 1
    return legoregebb.orszag