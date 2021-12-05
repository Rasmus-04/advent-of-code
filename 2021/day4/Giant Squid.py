with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))

num = f[0].split(",")
num = list(map(lambda x: int(x), num))

bords = []

temp = []
for i in f[2:]:
    i = i.split(" ")
    while True:
        if " " in i:
            i.remove(" ")
        elif "" in i:
            i.remove("")
        else:
            i = list(map(lambda x: int(x), i))
            if len(i) != 0:
                temp.append(i)
            else:
                bords.append(temp)
                temp = []
            break
bords.append(temp)



def answer():
    for iIndex in range(4, len(num)):
        for bordIndex, bord in enumerate(bords):
            for row in bord:
                bingo = 0
                for nummber in row:
                    if nummber in num[:iIndex + 1]:
                        bingo += 1
                        if bingo == 5:
                            return iIndex, bordIndex, row
            for i in range(5):
                bingo = 0
                for row in bord:
                    if row[i] in num[:iIndex + 1]:
                        bingo += 1
                        if bingo == 5:
                            return iIndex, bordIndex, row



ans = answer()


summa = 0
for i in bords[ans[1]]:
    for j in i:
        if j in num[:ans[0] + 1]:
            pass
        else:
            summa += j

final_answer = summa * num[ans[0]]
print(summa, final_answer)