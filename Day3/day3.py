


with open("input.txt", "r") as file:
    items = [i.strip() for i in file]


tot_score = 0
for rucksack in items:
    small, large = rucksack[:int(len(rucksack)/2)], rucksack[int(len(rucksack)/2):]
    for char in small:
        if char in large:
            if char.islower():
                tot_score += ord(char) - 96
            else:
                tot_score += ord(char) - 38          
            break

    
print(tot_score)


tot_score = 0
for i in range(3,len(items)+1,3):
    sub_set = items[i-3:i]
    print(sub_set)
    for i in sub_set[0]:
        if i in sub_set[0] and i in sub_set[1] and i in sub_set[2]:
            print("Found ", i)
            if i.islower():
                tot_score += ord(i) - 96
            else:
                tot_score += ord(i) - 38          
            break

print(tot_score)