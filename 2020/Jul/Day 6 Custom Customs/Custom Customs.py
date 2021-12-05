from string import ascii_lowercase


with open("Custom Customs.txt", "r") as f:
    f = f.readlines()


new_list = []
list2 = []
list3 = []

checklist = []

total_Yes = 0


for i in f:
    if len(i) >= 2:
        new_list.append(i.strip())
    else:
        new_list.append(i)


for j in new_list:
    if "\n" in j:
        list3.append(list2)
        list2 = []
    else:
        list2.append(j)

for j in list3:
    for k in j:
        for x in k:
            checklist.append(x)
    for l in ascii_lowercase:
        if checklist.count(l) == len(j):
            total_Yes += 1


    checklist = []





print(total_Yes)

#  12386 > pos