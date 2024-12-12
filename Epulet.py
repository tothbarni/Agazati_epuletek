class Epulet:
    def __init__(self, nev, varos, orszag, magassag, emelet, ev):
        self.nev = nev
        self.varos = varos
        self.orszag = orszag
        self.magassag = float(magassag.replace(',', '.'))  
        self.emelet = int(emelet)
        self.ev = int(ev)