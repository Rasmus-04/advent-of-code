with open("../input.txt", "r") as f:
    f = f.readlines()

f = f[0].split(",")

f = list(map(lambda x: int(x), f))

best_value = 0

for i in range(min(f),max(f)):
    print(i, max(f))
    fuil_req = 0
    for j in f:
        if j > i:
            for x in range(j-i + 1):
                fuil_req += x
        elif i > j:
            for x in range(i - j +1):
                fuil_req += x


    if i == min(f):
        best_value = fuil_req
    elif fuil_req < best_value:
        best_value = fuil_req

print(best_value)