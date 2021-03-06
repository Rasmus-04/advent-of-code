with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))



temp = []

ans = []

def get_answer(pos):
    row = pos[0]
    col = pos[1]

    if f[row][col] == "9" or pos in temp:
        return

    elif row == 0:
        if col == 0:
            temp.append(pos)
            get_answer((row + 1, col))
            get_answer((row, col + 1))
        elif col == len(f[0]) - 1:
            temp.append(pos)
            get_answer((row + 1, col))
            get_answer((row, col - 1))
        else:
            temp.append(pos)
            get_answer((row + 1, col))
            get_answer((row, col - 1))
            get_answer((row, col + 1))

    elif row == len(f) - 1:
        if col == 0:
            temp.append(pos)
            get_answer((row - 1, col))
            get_answer((row, col + 1))
        elif col == len(f[0]) - 1:
            temp.append(pos)
            get_answer((row - 1, col))
            get_answer((row, col - 1))
        else:
            temp.append(pos)
            get_answer((row - 1, col))
            get_answer((row, col - 1))
            get_answer((row, col + 1))

    else:
        if col == 0:
            temp.append(pos)
            get_answer((row + 1, col))
            get_answer((row, col + 1))
            get_answer((row - 1, col))
        elif col == len(f[0]) - 1:
            temp.append(pos)
            get_answer((row + 1, col))
            get_answer((row, col - 1))
            get_answer((row - 1, col))
        else:
            temp.append(pos)
            get_answer((row + 1, col))
            get_answer((row, col - 1))
            get_answer((row, col + 1))
            get_answer((row - 1, col))

    return


answer = []
for row in range(len(f)):
    for column in range(len(f[0])):
        if row == 0:
            if column == 0:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row][column + 1]:
                    answer.append((row, column))
            elif column == len(f[0]) - 1:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row][column - 1]:
                    answer.append((row, column))
            else:
                if f[row][column] < f[row][column-1] and f[row][column] < f[row][column + 1] and f[row][column] < f[row+1][column]:
                    answer.append((row, column))

        elif row == len(f) - 1:
            if column == 0:
                if f[row][column] < f[row][column + 1] and f[row][column] < f[row - 1][column]:
                    answer.append((row, column))
            elif column == len(f[0]) - 1:
                if f[row][column] < f[row -1][column] and f[row][column] < f[row][column-1]:
                    answer.append((row, column))
            else:
                if f[row][column] < f[row][column-1] and f[row][column] < f[row][column + 1] and f[row][column] < f[row-1][column]:
                    answer.append((row, column))
        else:
            if column == 0:
                if f[row][column] < f[row -1][column] and f[row][column] < f[row + 1][column] and f[row][column] < f[row][column + 1]:
                    answer.append((row, column))
            elif column == len(f[0]) - 1:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row-1][column] and f[row][column] < f[row][column-1]:
                    answer.append((row, column))
            else:
                if f[row][column] < f[row + 1][column] and f[row][column] < f[row - 1][column] and f[row][column] < f[row][column + 1] and f[row][column] < f[row][column - 1]:
                    answer.append((row, column))



for i in answer:
    temp.clear()
    get_answer(i)
    ans.append(len(temp))


x = 1
for i in sorted(ans)[:-4:-1]:
    x *= i

print(x)
