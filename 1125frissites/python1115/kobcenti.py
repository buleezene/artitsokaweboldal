kobcenti=int(input("Adja meg az autó köbcentijét:"))

if kobcenti > 8000:
    print(f'Az Ön által megadott {kobcenti} köbcenti túl nagy.')
else:
    if kobcenti < 3000:
        print(f'Az Ön által megadott {kobcenti} köbcenti alacsony kategória.')
    else:
        print(f'Az Ön által megadott {kobcenti} köbcenti magas kategória.')
