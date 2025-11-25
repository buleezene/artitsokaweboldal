file= open("idezet.txt", "r", encoding="utf-8")
szoveg= file.read()
file.close()
print(f'Sikeresen beolvastam a {file} tartalmát')

kereses= input("Mit szeretnél keresni a szövegben? ")

db= szoveg.count(kereses)

if kereses in szoveg:
    print("A keresett szöveg: ", kereses)
    print(f'A karaktersorozat: "{kereses}" {db} esetben fordult elő.')
else:
    print("A keresett szöveg: ", kereses)
    print(f'A "{kereses}" kifejezés nem szerepel az adott tartományban.')
