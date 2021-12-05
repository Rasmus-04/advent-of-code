"""
forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
"""

x, y, aim = 0, 0, 0

with open("input.txt", "r") as f:
    f = f.readlines()


f = list(map(lambda x:x.strip(),f))

for i in f:
    a, b = i.split()

    if a == "forward":
        x += int(b)
        y += (int(b) * aim)
    elif a == "down":
        aim += int(b)
    elif a == "up":
        aim -= int(b)


print(x * y)