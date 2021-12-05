with open("input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))
f = list(map(lambda x: x.split(" -> "), f))

lista = []
dup = []

def k_value(x1, y1, x2, y2):
    k = (y2 - y1) / (x2- x1)
    return k

print(len(f))
for indexx, i in enumerate(f):
    if indexx % 10 == 0:
        print(indexx)
    pos = list(map(lambda x: x.split(","), i))
    x1 = int(pos[0][0])
    y1 = int(pos[0][1])
    x2 = int(pos[1][0])
    y2 = int(pos[1][1])
    if x1 == x2:
        if y1 > y2:
            for x in range(y1 - y2 + 1):
                if (x1, y2 + x) in lista:
                    if (x1, y2 + x) not in dup:
                        dup.append((x1, y2 + x))
                else:
                    lista.append((x1, y2 + x))
        elif y2 > y1:
            for x in range(y2 - y1 + 1):
                if (x1, y1 + x) in lista:
                    if (x1, y1 + x) not in dup:
                        dup.append((x1, y1 + x))
                else:
                    lista.append((x1, y1 + x))
    elif y1 == y2:
        if x1 > x2:
            for x in range(x1 - x2 + 1):
                if (x2 + x, y2) in lista:
                    if (x2 + x, y2) not in dup:
                        dup.append((x2 + x, y2))
                else:
                    lista.append((x2 + x, y2))
        elif x2 > x1:
            for x in range(x2 - x1 + 1):
                if (x1 + x, y1) in lista:
                    if (x1 + x, y1) not in dup:
                        dup.append((x1 + x, y1))
                else:
                    lista.append((x1 + x, y1))
    else:
        while True:
            if (x2, y2) in lista:
                if (x2, y2) not in dup:
                    dup.append((x2, y2))
            else:
                lista.append((x2, y2))
            if x2 == x1 and y1 == y2:
                break
            if x2 < x1:
                x2 += 1
            else:
                x2 -= 1
            if y2 < y1:
                y2 += 1
            else:
                y2 -= 1


# x < 18627
print(len(dup))