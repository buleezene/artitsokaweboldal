"""
Dokumentációs komment:
Ez a program a feketeBt.txt állomány objektumorientált feldolgozásához készült
Készítette: Bőhm Balázs Antal
Budapest, 2026.11.26.
"""
print(__doc__)

class Dolgozo:
    def __init__ (self,sor):
        reszek=sor.split(":")
        self.nev=reszek[0]
        self.telepules=reszek[1]
        self.utca=reszek[2]
        self.fizetes=int(reszek[3])
        self.jutalom=int(reszek[4])
        self.szuletes=reszek[5]
        self.belepes=reszek[6]

#dolgozo=Dolgozo("Finch Zoltán:Miskolc:Kossuth u.61:220000:10000:1979-01-22:2009-01-26")
#print(f'Név: {dolgozo.nev}, született: {dolgozo.szuletes}')

dolgozok=[]

#file=open("feketeBt.txt", encoding="utf-8")
#szamlalo=0
#for sor in file:
#    if szamlalo>0:
#        dolgozo=Dolgozo(sor.strip())
#        dolgozok.append(dolgozo)
 #   szamlalo+=1
#file.close()
#print(len(dolgozok))
with open("feketeBt.txt", encoding="utf-8") as file:
    szamlalo=0
    for sor in file:
        if szamlalo>0:
            dolgozo=Dolgozo(sor.strip())
            dolgozok.append(dolgozo)
        szamlalo+=1


osszjovedelem=0
for dolgozo in dolgozok:
    if dolgozo.telepules=="Miskolc":
        osszjovedelem+=(dolgozo.fizetes+dolgozo.jutalom)

print(f'A miskolci dolgozók összes jövedelme: {osszjovedelem}')


file=open("hatvaniakAtlagfizetese.txt", "w")

osszfizetes=0
hatvanidb=0
for dolgozo in dolgozok:
    if dolgozo.telepules=="Hatvan":
        osszfizetes+=dolgozo.fizetes
        hatvanidb+=1
atlag=osszfizetes/hatvanidb
file.write(f'A hatvaniak átlagfizetése: {atlag}')
file.close()



