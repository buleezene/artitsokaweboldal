from vendeg import Vendeg

class Hotel:
    def olvas_fajl(self):
        fp = open('vendegek.txt', 'r')
        lines = fp.readlines()
        fp.close()
        self.vendegek = []
        for line in lines:
            (nev, erkezes, ar) = line.strip().split(':')
            vendeg = Vendeg(nev, erkezes, ar)
            self.vendegek.append(vendeg)

    def ir_fajlhoz(self, vendeg):
        fp = open('ujak.txt', 'a')  
        fp.write(vendeg.nev)
        fp.write(':')
        fp.write(vendeg.erkezes)
        fp.write(':')
        fp.write(str(vendeg.ar))  
        fp.write('\n')
        fp.close()

    def osszeg(self):
        return sum(v.ar for v in self.vendegek)

    def beker(self):
        nev = input("Vendég neve: ")
        erkezes = input("Érkezés dátuma (YYYY-MM-DD): ")
        ar = int(input("Fizetendő ár: "))
        vendeg = Vendeg(nev, erkezes, ar)
        self.vendegek.append(vendeg)
        self.ir_fajlhoz(vendeg)

    def kiir(self):
        for v in self.vendegek:
            print(f"{v.nev}, {v.erkezes}, {v.ar} Ft")

hotel = Hotel()
hotel.olvas_fajl()
print("Összes bevétel:", hotel.osszeg())
hotel.beker()
hotel.kiir()
