with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x:x.strip(),f))


print(f)


t = 0
for index, i in enumerate(f):
    if index == 0:
        continue
    if index == (len(f) - 1):
        pass

    if int(i) > int(f[index - 1]):
        t += 1

print(t)