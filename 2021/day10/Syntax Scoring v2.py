with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))

op = ["(", "[", "{", "<"]
cl = [")", "]", "}", ">"]

scores = []

for line in f:
    open_chunk = []
    close_chunk = []
    temp_score = 0

    for char_index, char in enumerate(line):
        if char in op:
            open_chunk.append(char)
            if char_index == len(line) -1:
                if char_index == len(line) - 1:
                    print(open_chunk)
                    for i in open_chunk[::-1]:
                        if i == "(":
                            temp_score = (temp_score * 5) + 1
                        elif i == "[":
                            temp_score = (temp_score * 5) + 2
                        elif i == "{":
                            temp_score = (temp_score * 5) + 3
                        elif i == "<":
                            temp_score = (temp_score * 5) + 4
                    scores.append(temp_score)
        else:
            if char == cl[op.index(open_chunk[-1])]:
                open_chunk = open_chunk[:-1]
                if char_index == len(line) - 1:
                    print(open_chunk)
                    for i in open_chunk[::-1]:
                        if i == "(":
                            temp_score = (temp_score * 5) + 1
                        elif i == "[":
                            temp_score = (temp_score * 5) + 2
                        elif i == "{":
                            temp_score = (temp_score * 5) + 3
                        elif i == "<":
                            temp_score = (temp_score * 5) + 4
                    scores.append(temp_score)
            else:
                #print("should have been", cl[op.index(open_chunk[-1])], "but found: ", char)
                break
scores = sorted(scores)

print(scores[int(len(scores)/2)])

"""
a = illegal_char.count(")") * 3
b = illegal_char.count("]") * 57
c = illegal_char.count("}") * 1197
d = illegal_char.count(">") * 25137
"""

#ans = a+b+c+d

#print(ans)