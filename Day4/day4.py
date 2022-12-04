
with open("input.txt", "r") as file:
    items = [(i.strip()).split(",") for i in file]

count = 0
for i in items:
    a,b = i
    a,b = a.split("-"), b.split("-")
    print(a,b)

    a = list(range(int(a[0]),int(a[1])+1))
    b = list(range(int(b[0]),int(b[1])+1))

    if (any(x in a for x in b)) or (any(x in b for x in a)):
        count += 1

print(count)
