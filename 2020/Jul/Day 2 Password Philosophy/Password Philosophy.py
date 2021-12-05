valid = 0
boy = 0
with open("Password Philosophy.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda y: y.strip(), f))



for l in f:
    password = l.partition(":")
    password = password[len(password) - 1]
    Split = l.partition("-")

    MinC = int(Split[0])

    MaxC = Split[2]
    MaxC = MaxC.partition(":")
    MaxC = MaxC[0]
    Letter = MaxC[-1]
    MaxC = int(MaxC[:-1])

    x = password.count(Letter)
    if x >= MinC and x <= MaxC:
        valid +=1


    if (Letter in password[MinC]) and (Letter not in password[MaxC]):
        boy += 1
    if (Letter not in password[MinC]) and (Letter in password[MaxC]):
        boy += 1



print(valid)

print(boy)


# 726>pos>407
