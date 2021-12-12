with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))

new_list = []

for i in f:
    temp = []
    for j in i:
        temp.append(int(j))
    new_list.append(temp)


flashes = 0

def flash_handle(row, col):
    global flashes
    flashes += 1

    new_list[row][col] = 0
    for row_ind in range(-1, 2):
        for col_ind in range(-1, 2):
            if row + row_ind < 0 or row + row_ind > 9:
                continue
            if col + col_ind < 0 or col + col_ind > 9:
                continue

            if new_list[row + row_ind][col + col_ind] < 10 and new_list[row + row_ind][col + col_ind] > 0:
                new_list[row + row_ind][col + col_ind] += 1


days = 100

for day in range(days):
    for row in range(len(new_list)):
        for col in range(len(new_list[0])):
            new_list[row][col] += 1

    while True:
        temp = 0
        for row in range(len(new_list)):
            for col in range(len(new_list[0])):
                if new_list[row][col] == 10:
                    temp += 1
                    flash_handle(row, col)
        if temp == 0:
            break

for i in new_list:
    print(i)

print(flashes)
