with open("Day 8 Handheld Halting.txt", "r") as s:
    s = s.readlines()
s = list(map(lambda y:y.strip(), f))

done = []
acc = 0
index = 0
stop = False
for ind, i in enumerate(s):
    with open("Day 8 Handheld Halting.txt", "r") as f:
            f = f.readlines()
    f = list(map(lambda y: y.strip(), f))

    if "nop " in i:
        x = f[ind].partition("nop ")
        värde = x[2]
        f[ind] = f"jmp {str(värde)}"

    elif "jmp " in i:
        x = f[ind].partition("jmp ")
        värde = x[2]
        f[ind] = f"nop {str(värde)}"


    while True:
        if index in done:
            stop = True
            break

        if index == len(f) - 1:
            print("Answer", acc)
            stop = True
            break

        if "acc " in f[index]:
            x = f[index].partition("acc ")
            värde = x[2]
            acc += int(värde)
            done.append(index)
            index += 1
            continue


        if "nop " in f[index]:
            done.append(index)
            index += 1
            continue

        if "jmp " in f[index]:
            x = f[index].partition("jmp ")
            värde = x[2]
            if int(värde) < 0:
                done.append(index)
                index -= abs(int(värde))
                continue
            done.append(index)
            index += int(värde)
            continue
    if stop:
        break

#   pos != 1849
