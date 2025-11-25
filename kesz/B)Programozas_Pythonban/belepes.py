print("Saját név: belepes.py")
print("Készítés dátuma: 2025.11.10.")
print("Osztályom: SZOFT1/1")

jelszo = input("A belépéshez adja meg a jelszót: ")
if jelszo != "titok":
    print("Helytelen jelszó")
    exit()

def jo_ar(ar):
    return ar <= 10000000


while True:
    ar = int(input("Adja meg a jármű árát (0 a kilépéshez): "))
    if ar == 0:
        print("Vége")
        break
    if jo_ar(ar):
        print("Jó ár")
    else:
        print("Túl drága")

            
