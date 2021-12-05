with open("day1text.txt", "r") as f:
    f = f.readlines()


f = list(map(lambda x:x.strip(),f))
# pos > 721

t = 0
for index, i in enumerate(f):
    if index == (len(f) - 3):
        break

    if (int(i) + int(f[index + 1]) + int(f[index + 2])) < (int(f[index + 1]) + int(f[index + 2]) + int(f[index + 3])):
        t += 1

print(t)