with open("../input.txt", "r") as f:
    f = f.readlines()

f = f[0].split(",")

f = list(map(lambda x: int(x), f))

age = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#age = {0: 0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0}

days = int(input("Days: "))


for i in f:
    age[i] += 1
print("Start values: ",age)

for i in range(days):
    new = []
    new.append(age[1])
    new.append(age[2])
    new.append(age[3])
    new.append(age[4])
    new.append(age[5])
    new.append(age[6])
    new.append(age[7] + age[0])
    new.append(age[8])
    new.append(age[0])
    age = new


print(sum(age))



