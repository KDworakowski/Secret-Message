#!/usr/bin/env python

import sys

def bitshift(x): #zmienia bity?
    bit = x << 1 #przesuniecie bitow
    movebit = bit & 255 #definiuje ze ten maksymalny bit to 255?
    if (x > 127): #jezeli x jest mniejsze niz 127
        new_movebit = movebit | 1 #nie wiem
    else:
        new_movebit = movebit #new_movebit ma teraz wartość movebit
    return (new_movebit) #zwroc wartosc new_movebit

def prepare(x):
    table = [] #definiuje zmienna table

    for i in x:
        table.append(ord(i)) #dodaje do tabeli ord(i), nie wiem co to
    return table #zwraca wynik tabeli

def convert(table, outTable):
    index = 0

    for chars in table: #dla znakow w tabeli
        if index == 0: #jezeli jest 0 znakow
            index += 1 #dodaj do indexa 1? nie jestem pewny co oznacza "+="
            pass
        else:
            lol = bitshift(int(outTable[index-1]) ^ int(chars)) #zmienna lol to definicja bitshift ktora wykonuje outTable index - 1 w listy xor liczba z listy
            outTable.append(lol) #do "outTable" dodaj "lol"
            index += 1

    return outTable #zwroc outTable

def decToHex(table):
    out = "" #zmienna out to ""

    for i in table:
        x = hex(i) #zmienna x to hex(i)
        val = x[2:] #zmienna val to x[2:]

        if(i > 9) and (i < 16):
            out = out + "0" + val
        else:
            if (i<10):
                out = out + "0" + val
            else:
                out = out + val
    return out

def main():
    value = sys.argv[1]
    # value = "0"
# 0>94
# 01>944b
# 012>944bf2
    inputTable = prepare(value)
    outputTable = []
    key = []

    key.append(ord("z"))

    lol = bitshift(int(key[0]) ^ int(inputTable[0]))

    # tmp = int(key[0]) ^ int(inputTable[0])
    # lol = bitshift(tmp)

    outputTable.append(lol)
    outputTable = convert(inputTable, outputTable)
    out = decToHex(outputTable)

    print(out)

if __name__ == '__main__':
    main()

# 97 (a) ^ 48 (0) = 81; 81 << 1 = 162 (a2);

# z -> 122; 0 -> 48; 122 ^ 48 -> 74; 74 << 1 -> 148; 148 & 255 -> 148; (dec to hex) 148 -> 94;

# z -> 122; 0 -> 48; 122 ^ 48 -> 74; 74 << 1 -> 148; 148 & 255 -> 148; 148 -> 94
# z -> 122; 1 -> 49; 122 ^ 49 -> 165; 165 << 1 -> 330; 330 & 255 -> 74; 74 | 1 -> 75; 75 -> 4b

# z -> 122; 0 -> 48; 122 ^ 48 -> 74; 74 << 1 -> 148; 148 & 255 -> 148; 148 -> 94
# z -> 122; 1 -> 49; 122 ^ 49 -> 165; 165 << 1 -> 330; 330 & 255 -> 74; 74 | 1 -> 75; 75 -> 4b
# z -> 122; 2 -> 50; 122 ^ 50 -> 121; 121 << 1 -> 242;  242 & 255 -> 255; 242 -> f2


# table - 0 -> 48
# key - z -> 122
# key(122) ^ table(48) -> 74
# x(74) << 1 -> bit(148)
# bit(148) & 255 -> 148
# (x=0x94)
# outputtable(148) -> out(94)




# 0 zmienia sie w 48
# bit to 148
# x to 74
# 0 zmienia sie w 148