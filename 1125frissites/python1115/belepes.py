def elfogadhato_ar(ar):
    return ar <= 10_000_000

def main():
    print("Program neve: belepes.py")
    print("Készítette: BBA")
    print("Dátum: 2025.11.24")
    print("Osztály: 2025-2026 SZOFT I/1/E")

    jelszo = input("Kérlek add meg a jelszót: ")
    if jelszo != "titok":
        print("Helytelen jelszó. Kilépés...")
        return

    while True:
        try:
            ar = int(input("Add meg a jármű árát (0 a kilépéshez): "))
            if ar == 0:
                print("Kilépés...")
                break
            if elfogadhato_ar(ar):
                print("Jó ár")
            else:
                print("Túl magas")
        except ValueError:
            print("Kérlek egész számot adj meg!")

if __name__ == "__main__":
    main()
