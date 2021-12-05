nums = []
sum = 0

with open("lists", "r") as f:
    t = f.readlines()
    t = list(map(lambda s: s.strip(), t))

for num in t:
    nums.append(int(num))

for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                sum = i * j * k
                print(f"{i} * {j} * {k} = {sum}")
                break
        if sum > 0:
            break