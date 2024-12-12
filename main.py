import bevezetes
import sorozat
import epuletek
"""print("I/A:")
bevezetes.jatekos()

print("\nI/A, B, C:")
dobasok = sorozat.fej_iras()

print("\nII/D, E:")
db = sorozat.fejek_szama(dobasok)
sorozat.konzol_kiir("A fejek száma: ", db)

sorozat.file_kiir(db)
"""


epuletek.beolvas()

print("\nIII/A, B:")
db = epuletek.epuletek_szama(epuletek)
print(f"tAz épületek száma: {db}")

print("\nIII/C:")
db2 = epuletek.magas_epuletek_szama(epuletek)
print(f"Az 555 lábnál magasabb épületek száma: {db2}")

print("\nIII/D:")
old = epuletek.legoregebb_epulet_orszaga(epuletek)
print(f"A legöregebb épület országa: {old}")