nummers = {0:["c", "a", "g", "e", "d", "b"], 1:["a", "b"], 2:["g", "c", "d", "f", "a"], 3:["f", "b", "c", "a", "d"],
           4:["e", "a", "f", "b"], 5:["c", "d", "f", "b", "e"], 6:["c", "d", "f", "g", "e", "b"],
           7:["d", "a", "b"], 8:["a", "c", "e", "d", "g", "f", "b"], 9:["c", "e", "f", "a", "b", "d"]}



final_value = 0

line = "fcgedb"
output = line.split(" ")
# i = each output number
number = ""
for i in output:
    # j = index for number

    for j in nummers:
        test = 0
        if len(i) == len(nummers[j]):
            # char = letter in output
            for char in i:
                if char in nummers[j]:
                    test += 1
        if test == len(nummers[j]):
            number += str(j)


print(number)