with open("../input.txt", "r") as f:
    f = f.readlines()

f = list(map(lambda x: x.strip(), f))

op = ["(", "[", "{", "<"]
cl = [")", "]", "}", ">"]

illegal_char = []

for line in f:
    open_chunk = []
    for char_index, char in enumerate(line):
        if char in op:
            open_chunk.append(char)
        else:
            if char == cl[op.index(open_chunk[-1])]:
                open_chunk = open_chunk[:-1]
            else:
                #print("should have been", cl[op.index(open_chunk[-1])], "but found: ", char)
                illegal_char.append(char)
                break

a = illegal_char.count(")") * 3
b = illegal_char.count("]") * 57
c = illegal_char.count("}") * 1197
d = illegal_char.count(">") * 25137

ans = a+b+c+d

print(ans)