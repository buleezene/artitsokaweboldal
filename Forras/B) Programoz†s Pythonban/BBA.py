while True:
    sz1=int(input("Adjon meg egy számot 10 és 99 között:"))
    sz2=int(input("Adjon meg egy másik számot 10 és 99 között:"))

    if sz1 >= 10 and sz1 < 100 and sz2 >= 10 and sz2 < 100 and sz1 != sz2:
        break
    else:
        print("Hibás érték! Mind a két szám 10 és 99 között legyen, és ne legyenek azonosak.")

kisebb= min(sz1, sz2)
nagyobb= max(sz1, sz2)

print (f' A két szám közötti négyzet számok: ')
for i in range(kisebb, nagyobb +1):
    print(f' {i}^2 = {i*i}')
