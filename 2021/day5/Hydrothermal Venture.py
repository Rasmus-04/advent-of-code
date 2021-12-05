with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))
f = list(map(lambda x: x.split(" -> "), f))

lista = []

def k_value(x1, y1, x2, y2):
    k = (y2 - y1) / (x2- x1)
    return k


for i in f:
    pos = list(map(lambda x: x.split(","), i))
    x1 = int(pos[0][0])
    y1 = int(pos[0][1])
    x2 = int(pos[1][0])
    y2 = int(pos[1][1])
    if x1 == x2:
        if y1 > y2:
            for x in range(y1 - y2 + 1):
                lista.append((x1, y2 + x))
        elif y2 > y1:
            for x in range(y2 - y1 + 1):
                lista.append((x1, y1 + x))
    elif y1 == y2:
        if x1 > x2:
            for x in range(x1 - x2 + 1):
                lista.append((x2 + x, y2))
        elif x2 > x1:
            for x in range(x2 - x1 + 1):
                lista.append((x1 + x, y1))
    else:
        while True:
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



duplicate = []

for index, i in enumerate(lista):
    print(index)
    if i in duplicate:
        continue
    else:
        if lista.count(i) > 1:
            duplicate.append(i)

print(len(duplicate))