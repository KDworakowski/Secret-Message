#!/usr/bin/env python

import sys

def bitshift(x):
    if (x < 127) and (x % 2 == 1):
        x += 255
    return x >> 1
    

def chunks(list_in, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(list_in), n):
        # Create an index range for l of n items:
        yield list_in[i:i+n]
# then just do this to get your output

def prepare(x):
    table = list(chunks(x, 2))
    outTable = []
    for i in table:
        outTable.append(int(i, 16))
    return outTable

def convert(table, outTable):
    index = 0

    for chars in table: #dla znakow w tabeli
        if index == 0: #jezeli jest 0 znakow
            index += 1 #dodaj do indexa 1? nie jestem pewny co oznacza "+="
            pass
        else:
            lol = int(table[index-1]) ^ (bitshift(int(chars))) #zmienna lol to definicja bitshift ktora wykonuje outTable index - 1 w listy xor liczba z listy
            outTable.append(lol) #do "outTable" dodaj "lol"
            index += 1

    return outTable #zwroc outTable

def hexToDec(table):
    out = ""
    for i in table:
        out += chr(i)
    return out

def main():
    value = sys.argv[1]
    # value = "944bf2"

    inputTable = prepare(value)
    outputTable = []
    key = []

    key.append(ord("z"))

    lol = (int(key[0])) ^ bitshift(int(inputTable[0]))

    outputTable.append(lol)
    outputTable = convert(inputTable, outputTable)
    out = hexToDec(outputTable)

    print(out)
    # print(outputTable)

if __name__ == '__main__':
    main()


# z -> 122; 0 -> 48; 122 ^ 48 -> 74; 74 << 1 -> 148; 148 & 255 -> 148; (dec to hex) 148 -> 94;

# z -> 122; 0 -> 48; 122 ^ 48 -> 74; 74 << 1 -> 148; 148 & 255 -> 148; 148 -> 94
# z -> 122; 1 -> 49; 122 ^ 49 -> 165; 165 << 1 -> 330; 330 & 255 -> 74; 74 | 1 -> 75; 75 -> 4b

# z -> 122; 0 -> 48; 122 ^ 48 -> 74; 74 << 1 -> 148; 148 & 255 -> 148; 148 -> 94
# z -> 122; 1 -> 49; 122 ^ 49 -> 165; 165 << 1 -> 330; 330 & 255 -> 74; 74 | 1 -> 75; 75 -> 4b
# z -> 122; 2 -> 50; 122 ^ 50 -> 121; 121 << 1 -> 242;  242 & 255 -> 255; 242 -> f2