
with open("input.txt", "r") as f:
    stream = f.readline().strip()


def is_unique(s):
    if all(list(map(lambda x: s.count(x) == 1, s))):
        return True
    return False


length = None
for i, j in enumerate(stream):
    if is_unique(stream[i:i+4]):
        length = i+14
        break


print("First start marker: ", length)

for i, j in enumerate(stream):
    if is_unique(stream[i:i+14]):
        length = i+14
        break

print("First message: ", length)
