with open("Toboggan Trajectory.txt", "r") as f:
    f = f.readlines()


pos = 0
tree = 0
f = list(map(lambda y: y.strip(), f))
for index, l in enumerate(f[1:]):
    #print(index + 2, end=" ")
    pos += 3
    if pos >= len(l):
        pos = pos - 31

    if l[pos] == "#":
        #print(l[pos], pos)
        tree += 1
        continue
    #print()
print("tree", tree)

pos = 0
tree1 = 0
for index, l in enumerate(f[1:]):
    #print(index + 2, end=" ")
    pos += 1
    if pos >= len(l):
        pos = pos - 31

    if l[pos] == "#":
        #print(l[pos], pos)
        tree1 += 1
        continue
    #print()
print("tree1", tree1)

pos = 0
tree2 = 0
for index, l in enumerate(f[1:]):
    #print(index + 2, end=" ")
    pos += 5
    if pos >= len(l):
        pos = pos - 31

    if l[pos] == "#":
        #print(l[pos], pos)
        tree2 += 1
        continue
    #print()
print("tree3", tree2)

pos = 0
tree3 = 0
for index, l in enumerate(f[1:]):
    #print(index + 2, end=" ")
    pos += 7
    if pos >= len(l):
        pos = pos - 31

    if l[pos] == "#":
        #print(l[pos], pos)
        tree3 += 1
        continue
    #print()
print("tree4", tree3)


pos = 0
tree4 = 0
for index, l in enumerate(f[1:]):

    if index % 2 == 0:
        continue

    #print(index + 2, end=" ")
    pos += 1
    if pos >= len(l):
        pos = pos - 31

    if l[pos] == "#":
        #print(l[pos], pos)
        tree4 += 1
        continue
    #print()
print("tree4", tree4)

print("Answer =", tree * tree1 * tree2 * tree3 * tree4)
