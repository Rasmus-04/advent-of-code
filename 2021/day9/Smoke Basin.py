with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))

answer = 0
for row in range(len(f)):
    for column in range(len(f[0])):
        if row == 0:
            if column == 0:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row][column + 1]:
                    answer += int(f[row][column]) + 1
            elif column == len(f[0]) - 1:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row][column - 1]:
                    answer += int(f[row][column]) + 1
            else:
                if f[row][column] < f[row][column-1] and f[row][column] < f[row][column + 1] and f[row][column] < f[row+1][column]:
                    answer += int(f[row][column]) + 1

        elif row == len(f) - 1:
            if column == 0:
                if f[row][column] < f[row][column + 1] and f[row][column] < f[row - 1][column]:
                    answer += int(f[row][column]) + 1
            elif column == len(f[0]) - 1:
                if f[row][column] < f[row -1][column] and f[row][column] < f[row][column-1]:
                    answer += int(f[row][column]) + 1
            else:
                if f[row][column] < f[row][column-1] and f[row][column] < f[row][column + 1] and f[row][column] < f[row-1][column]:
                    answer += int(f[row][column]) + 1
        else:
            if column == 0:
                if f[row][column] < f[row -1][column] and f[row][column] < f[row + 1][column] and f[row][column] < f[row][column + 1]:
                    answer += int(f[row][column]) + 1
            elif column == len(f[0]) - 1:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row-1][column] and f[row][column] < f[row][column-1]:
                    answer += int(f[row][column]) + 1
            else:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row - 1][column] and f[row][column] < f[row][column + 1] and f[row][column] < f[row][column - 1]:
                    answer += int(f[row][column]) + 1


print(answer)