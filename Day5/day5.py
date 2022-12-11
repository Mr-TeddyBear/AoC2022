import numpy as np

with open("input.txt", "r") as file:
    stacks = []
    for i in range(9):
        stacks.append(((file.readline()).strip()).split())
    file.readline()
    moves = [f.strip() for f in file]

stacks = stacks[:-1]
stacks = (np.transpose(stacks))
stacks = list(map(lambda x: list(x[::-1]), stacks))
stacks = list(map(lambda x: [j for j in x if j != "..."], stacks))

moves = list(map(lambda x: (x.split()), moves))
moves = list(map(lambda x: [x[i] for i in range(len(x)) if i % 2 != 0], moves))
moves = list(map(lambda x: list(map(lambda y: int(y), x)), moves))

[print(j) for j in stacks]
for i in moves:
    # try:
    if (l := len(stacks[i[1]-1])) < i[0]:
        i[0] = l

    stacks[i[2]-1] = stacks[i[2]-1] + stacks[i[1]-1][-(i[0]):]
    stacks[i[1]-1] = stacks[i[1]-1][:-(i[0])]
    # except:
    # print("Move:", i)
    # [print(j) for j in stacks]
    # exit()
print("After:")
[print(i) for i in stacks]
print("First in all stacks")
print(stacks[:][-1])
print(("".join([i[-1] for i in stacks]).replace("[", "")).replace("]", ""))
print([i[-1] for i in stacks])
