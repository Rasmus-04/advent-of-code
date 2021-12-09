with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))
f = list(map(lambda x: x.split(" | "), f))

current_state = [[], [], [], [], [], [], []]
nummers = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

#test = "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc"

#test = test.split(" | ")


def get_state(test):
    while True:
        for seq in test[0].split(" "):

            # number 1
            if len(seq) == 2 and len(current_state[2]) == 0:
                for char in seq:
                    current_state[2].append(char)
                    current_state[5].append(char)

            # number 7
            elif len(seq) == 3 and len(current_state[2]) != 0 and len(current_state[0]) == 0:
                for char in seq:
                    if char not in current_state[2]:
                        current_state[0].append(char)
                        break

            # number 4
            elif len(seq) == 4 and len(current_state[2]) != 0 and len(current_state[0]) != 0:
                for char in seq:
                    if char not in current_state[2]:
                        current_state[3].append(char)
                        current_state[1].append(char)

            # number 5
            elif len(seq) == 5 and len(current_state[2]) != 0 and len(current_state[3]) != 0 and len(current_state[5]) != 1:
                for char in current_state[2]:
                    if char not in seq:
                        temp = 0
                        for j in current_state[1]:
                            if j in seq:
                                temp += 1
                        # confirmed number 5
                        if temp == 2:
                            for i in current_state[2]:
                                if i in seq:
                                    current_state[5] = [i]
                                    current_state[2].remove(i)

            # number 3
            elif len(seq) == 5 and len(current_state[5]) == 1:
                if current_state[2][0] in seq and current_state[5][0] in seq:
                    for i in current_state[3]:
                        if i not in seq:
                            current_state[1] = [i]
                            current_state[3].remove(i)
                    for i in seq:
                        if i not in current_state[0] and i not in current_state[2] and i not in current_state[3] and i not in current_state[5]:
                            current_state[6] = [i]
                            for x in "abcdefg":
                                if x not in current_state[0] and x not in current_state[1] and x not in current_state[2] and x not in current_state[3] and x not in current_state[5] and x not in current_state[6]:
                                    current_state[4] = [x]
                                    return

def make_code():
    nummers[0] = [current_state[0][0], current_state[1][0], current_state[2][0], current_state[4][0], current_state[5][0], current_state[6][0]]
    nummers[1] = [current_state[2][0], current_state[5][0]]
    nummers[2] = [current_state[0][0], current_state[2][0], current_state[3][0], current_state[4][0], current_state[6][0]]
    nummers[3] = [current_state[0][0], current_state[2][0], current_state[3][0], current_state[5][0], current_state[6][0]]
    nummers[4] = [current_state[1][0], current_state[2][0], current_state[3][0], current_state[5][0]]
    nummers[5] = [current_state[0][0], current_state[1][0], current_state[3][0], current_state[5][0], current_state[6][0]]
    nummers[6] = [current_state[0][0], current_state[1][0], current_state[3][0], current_state[4][0], current_state[5][0], current_state[6][0]]
    nummers[7] = [current_state[0][0], current_state[2][0], current_state[5][0]]
    nummers[8] = [current_state[0][0], current_state[1][0], current_state[2][0], current_state[3][0], current_state[4][0], current_state[5][0], current_state[6][0]]
    nummers[9] = [current_state[0][0], current_state[1][0], current_state[2][0], current_state[3][0], current_state[5][0], current_state[6][0]]

def reset():
    global current_state, nummers
    current_state = [[], [], [], [], [], [], []]
    nummers = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}


ans = 0
for y in f:
    reset()
    get_state(y)
    make_code()
    nr = ""
    for seq in y[1].split(" "):
        for i in nummers:
            temp = 0
            if len(seq) == len(nummers[i]):
                for char in seq:
                    if char in nummers[i]:
                        temp += 1
                if temp == len(nummers[i]):
                    nr += str(i)
    ans += int(nr)

print(ans)