beker=int(input("Add meg a jármű köbcentijét: "))

if beker >= 8000:
    print("Túl nagy")
    
else:
    if beker<= 3000:
        print("Alacsony kategória")
    else:
        print("Magas kategória")


