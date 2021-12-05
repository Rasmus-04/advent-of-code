
with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))


def oxygen():
    criteria = ""
    for y in range(len(f[0])):
        one = 0
        zero = 0

        counter = 0
        correct = ""

        for i in f:
            if i[:len(criteria)] != criteria:
                continue
            if i[y] == "1":
                one += 1
            else:
                zero += 1
            counter += 1
            if counter == 1:
                correct += i
        if counter == 1:
            return correct

        if one >= zero:
            criteria += "1"
        else:
            criteria += "0"

    return criteria


def CO2():
    criteria = ""
    for y in range(len(f[0])):
        one = 0
        zero = 0

        counter = 0
        correct = ""

        for i in f:
            if i[:len(criteria)] != criteria:
                continue
            if i[y] == "1":
                one += 1
            else:
                zero += 1
            counter += 1
            if counter == 1:
                correct += i
        if counter == 1:
            return correct

        if one >= zero:
            criteria += "0"
        else:
            criteria += "1"

    return criteria


def convert(inp):
    ans = 0
    for index, i in enumerate(inp[::-1]):
        if i == "1":
            ans += 2**index

    return ans





print(oxygen(), convert(oxygen()))
print(CO2(), convert(CO2()))

life_support_rating = convert(oxygen()) * convert(CO2())

print(life_support_rating)