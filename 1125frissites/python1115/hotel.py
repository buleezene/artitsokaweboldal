#import vendeg #ilyenkor a későbbi hivatkozás: vendeg.Vendeg
from vendeg import Vendeg #ilyenkor viszont: Vendeg is elegendő
class Hotel:
    def olvas_fajl(self):
        #fp = open('adat.txt', 'r')
        fp = open('vendegek.txt', 'r')
        lines = fp.readlines()
        fp.close()
        self.vendegek = []
        for line in lines:
            (nev, erkezes, ar) = line.split(':')
            vendeg = Vendeg(nev, erkezes, ar)
            self.vendegek.append(vendeg)
        #return "Beolvasás kész"
            
    def ir_fajlhoz(self, vendeg):
        fp1=open("vendegek.txt","a")
        fp2 = open('ujak.txt', 'w')
        fp1.write(vendeg.nev)
        fp2.write(vendeg.nev)
        fp1.write(':')
        fp2.write(':')
        fp1.write(vendeg.erkezes)
        fp2.write(vendeg.erkezes)
        fp1.write(':')
        fp2.write(':')
        fp1.write(str(vendeg.ar))
        fp2.write(str(vendeg.ar))
        fp1.write('\n')
        fp2.write('\n') 
        fp1.close()
        fp2.close()

##    def osszeg(self):
##        pass
    def osszeg(self):
        ossz=0
        for vendeg in self.vendegek:
            ossz+=vendeg.ar
        return ossz
        
    def beker(self):
        nev=input("Név: ")
        erkezes=input("Érkezés: ")
        while True:
            try:
                ar=int(input("Ár: "))
                break
            except:
                pass#continue
        vendeg=Vendeg(nev,erkezes,ar)
        self.ir_fajlhoz(vendeg)

    def kiir(self):
        for vendeg in self.vendegek:
            #print(vendeg)
            print(f"Név: {vendeg.nev}, Érkezés: {vendeg.erkezes}, Ár: {vendeg.ar}")
        
        
    

##    def __str__(self):
##        valasz="Ez egy Hotel osztályból létrejött példány"
##        return valasz
##    def __repr__(self):
##        valasz="REPR: Ez egy Hotel osztályból létrejött példány"
##        return valasz


hotel=Hotel()
#print(hotel.olvas_fajl())
hotel.olvas_fajl()
print(hotel.osszeg())

##def beker():
##    nev=input("Név: ")
##    erkezes=input("Érkezés: ")
##    ar=input("Ár: ")
##
##beker()
hotel.kiir()

