

class Vendeg:
    def __init__(self, nev, erkezes, ar):
        self.nev = nev
        self.erkezes = erkezes
        self.ar = int(ar) 


    def __str__(self):
        return f"{self.nev}, {self.erkezes}, {self.ar} Ft"


from vendeg import Vendeg


class Hotel:
    def __init__(self):
        self.vendegek = []


    def olvas_fajl(self):
        with open("vendegek.txt", "r", encoding="utf-8") as fajl:
            for sor in fajl:
                adatok = sor.strip().split(",")
                if len(adatok) == 3:
                    nev, erkezes, ar = adatok
                    self.vendegek.append(Vendeg(nev, erkezes, ar))


    def osszeg(self):
        return sum(v.ar for v in self.vendegek)


    def beker(self):
        nev = input("Vendég neve: ")
        erkezes = input("Érkezés dátuma: ")
        ar = int(input("Fizetendő ár: "))
        uj_vendeg = Vendeg(nev, erkezes, ar)
        self.vendegek.append(uj_vendeg)
        self.ir_fajlhoz(uj_vendeg)


    def ir_fajlhoz(self, vendeg):
        with open("vendegek.txt", "a", encoding="utf-8") as fajl:
            fajl.write(f"{vendeg.nev},{vendeg.erkezes},{vendeg.ar}\n")

    def kiir(self):
        for vendeg in self.vendegek:
            print(vendeg)

hotel = Hotel()
hotel.olvas_fajl()
print("Összes fizetendő összeg:", hotel.osszeg(), "Ft")
hotel.beker()
hotel.kiir()

