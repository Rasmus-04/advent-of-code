with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))
f = list(map(lambda x: x.split(" | "), f))


nummers = {0:["c", "a", "g", "e", "d", "b"], 1:["a", "b"], 2:["g", "c", "d", "f", "a"], 3:["f", "b", "c", "a", "d"],
           4:["e", "a", "f", "b"], 5:["c", "d", "f", "b", "e"], 6:["c", "d", "f", "g", "e", "b"],
           7:["d", "a", "b"], 8:["a", "c", "e", "d", "g", "f", "b"], 9:["c", "e", "f", "a", "b", "d"]}


count = 0

for line in f:
    output = line[1].split(" ")
    for i in output:
        if len(i) == len(nummers[1]):
            count += 1
        elif len(i) == len(nummers[4]):
            count += 1
        elif len(i) == len(nummers[7]):
            count += 1
        elif len(i) == len(nummers[8]):
            count += 1

print(count)