from string import ascii_lowercase, ascii_uppercase


with open("Passport Processing.txt", "r") as f:
    f = f.readlines()


new_list = []
list2 = []
list3 = []
val = 0
valid = 0
test = 0

for i in f:
    if len(i) > 2:
        new_list.append(i.strip())
    else:
        new_list.append(i)


for j in new_list:
    if "\n" in j:
        list3.append(list2)
        list2 = []
    else:
        list2.append(j)

for a in list3:
    for j in a:
        if "byr:" in j:
            pp = j.partition("byr:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]

            if 1920 <= int(pp) <= 2002 and len(pp) == 4:
                val += 1

        if "iyr:" in j:
            pp = j.partition("iyr:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]
            if 2010 <= int(pp) <= 2020 and 4 == len(pp):
                val += 1

        if "eyr:" in j:
            pp = j.partition("eyr:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]
            if 2020 <= int(pp) <= 2030 and 4 == len(pp):
                val += 1

        if "hgt:" in j:
            pp = j.partition("hgt:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]

            if pp[-2:] == "cm":
                if 150 <= int(pp[:-2]) <= 193:
                    val += 1

            elif pp[-2:] == "in":
                if 59 <= int(pp[:-2]) <= 76:
                    val += 1

        if "hcl:" in j:
            pp = j.partition("hcl:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]

            if len(pp) == 7 and pp[0] == "#":
                val += 1
                for g in ascii_lowercase[6:]:
                    if g in pp:
                        val -= 1
                        break




        if "ecl:" in j:
            pp = j.partition("ecl:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]

            if pp == "amb":
                val += 1
            if pp == "blu":
                val += 1
            if pp == "brn":
                val += 1
            if pp == "gry":
                val += 1
            if pp == "grn":
                val += 1
            if pp == "hzl":
                val += 1
            if pp == "oth":
                val += 1

        if "pid" in j:
            pp = j.partition("pid:")
            try:
                pp = pp[2].partition(" ")
            except:
                pass
            pp = pp[0]

            if len(pp) == 9:
                val += 1











    if val > 6:
        valid += 1
        val = 0
    else:
        val = 0

print(valid)
print(test)
