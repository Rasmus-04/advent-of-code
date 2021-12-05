with open("Binary Boarding.txt", "r") as f:
    f = f.readlines()
f = list(map(lambda y:y.strip(), f))

for i in range(len(f)):
    row = int(f[i][:7].replace("F", "0").replace("B", "1"), 2)
    column = int(f[i][7:].replace("L", "0").replace("R", "1"), 2)
    f[i] = (8 * row) + column
f.sort()

print("Part 1: ", max(f))
for i in range(len(f) - 1):
    if int(f[i] + 1) != int(f[i + 1]):
        print("Part 2: ", int(f[i] + 1))


"""
with open("Binary Boarding.txt", "r") as f:
    f = f.readlines()
f = list(map(lambda y: y.strip(), f))


row1 = 127
row2 = 0
finalrow = 0
column1 = 7
column2 = 0
finalcolumn = 0
seatID = []


for l in f:
    for index, j in enumerate(l):
        if j == "F":
            if index == 0:
                row1 = int((row1 - row2/2)/2)
            else:
                row1 = row1 - round((row1 - row2) / 2)


            finalrow = row2

            #print(index + 1, "f", row2, " ", row1)


        elif j == "B":
            if index == 0:
                row2 = round(row1/2)
            elif index != len(j) - 1:
                row2 = round(((row1 - row2)/2) + row2)
            else:
                finalrow = row1
            finalrow = row1
            #print(index + 1, "B", row2, " ", row1)


        elif j == "R":
            if index != len(l) - 1:
                column2 = round(column1/2)

            finalcolumn = column1

            #print(index + 1, "R", column2, column1)


        elif j == "L":
            if index != len(l) - 1:
                column1 = column1 - round((column1 - column2)/2)

            finalcolumn = column2
            #print(index + 1, "L", column2, column1)




    seatID.append(finalrow * 8 + finalcolumn)

    row1 = 127
    row2 = 0
    finalrow = 0
    column1 = 7
    column2 = 0
    finalcolumn = 0


seatID.sort()
print(seatID)

# 135
"""