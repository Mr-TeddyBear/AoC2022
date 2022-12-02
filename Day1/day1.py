
#Part1
with open("input.txt", "r") as f:
    print(max(map(lambda x: sum(list(map(lambda c: int(c), x.split()))), " ".join([i.strip() for i in f]).split("  "))))

#Part2
with open("input.txt", "r") as f:
    print(sum(sorted(list(map(lambda x: sum(list(map(lambda c: int(c), x.split()))), " ".join([i.strip() for i in f]).split("  "))))[-3:]))

