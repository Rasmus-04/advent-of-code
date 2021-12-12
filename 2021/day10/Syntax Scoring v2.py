with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))

op = ["(", "[", "{", "<"]
cl = [")", "]", "}", ">"]

scores = []

def get_score(open_chunk):
    temp_score = 0
    for i in open_chunk[::-1]:
        if i == "(":
            temp_score = (temp_score * 5) + 1
        elif i == "[":
            temp_score = (temp_score * 5) + 2
        elif i == "{":
            temp_score = (temp_score * 5) + 3
        elif i == "<":
            temp_score = (temp_score * 5) + 4
    return temp_score

for line in f:
    open_chunk = []

    for char_index, char in enumerate(line):
        if char in op:
            open_chunk.append(char)
            if char_index == len(line) - 1:
                scores.append(get_score(open_chunk))

        else:
            if char == cl[op.index(open_chunk[-1])]:
                open_chunk = open_chunk[:-1]
                if char_index == len(line) - 1:
                    scores.append(get_score(open_chunk))
            else:
                #print("should have been", cl[op.index(open_chunk[-1])], "but found: ", char)
                break
scores = sorted(scores)

print(scores[int(len(scores)/2)])
