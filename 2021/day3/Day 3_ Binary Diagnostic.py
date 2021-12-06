oxygen = ""
CO2 = ""

with open("input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x:x.strip(),f))


def answer():
    global oxygen, CO2
    for y in range(12):
        one = 0
        zero = 0
        for i in f:
            if i[y] == "1":
                one += 1
            else:
                zero += 1

        if one > zero:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            epsilon_rate += "1"
            gamma_rate += "0"


def convert(inp):
    ans = 0

    for index, i in enumerate(inp[::-1]):
        if i == "1":
            ans += 2**index

    return ans


answer()

print(convert(oxygen) * convert(CO2))
