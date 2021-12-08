with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))
f = list(map(lambda x: x.split("|"), f))

for i in f:
    for j in i:
        for x in j.split(" "):
            print(j)