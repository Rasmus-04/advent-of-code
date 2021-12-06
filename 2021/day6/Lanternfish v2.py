with open("../input.txt", "r") as f:
    f = f.readlines()

f = f[0].split(",")

f = list(map(lambda x: int(x), f))

days = int(input("Days: "))


for i in range(days):
    print(i, len(f))
    ny_lista = []
    for i in f:
        if i == 0:
            ny_lista.append(8)
            ny_lista.append(6)
        else:
            ny_lista.append(i-1)
    f = ny_lista
    ny_lista = []

print(len(f))
