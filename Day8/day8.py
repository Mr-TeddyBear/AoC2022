import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


with open("test_input.txt", "r") as f:
    trees = np.array([np.array([int(j) for j in list(i.strip())]) for i in f])

print(trees)

count = 0

for i,j in enumerate(trees[1:-1]):
    i += 1
    for k,l in enumerate(j[1:-1]):
        k += 1

        if any([np.all(trees[i,k] > trees[:i,k]), np.all(trees[i,k] > trees[i+1:,k]), np.all(trees[i,k] > trees[i,:k]), np.all(trees[i,k] > trees[i,k+1:])]):
            count += 1

count += trees.shape[0]*2 + trees.shape[1]*2 - 4
print(f"Number of trees visible from outside {count}")

max_score = np.zeros_like(trees)



for i,j in enumerate(trees[1:-1]):
    i += 1
    for k,l in enumerate(j[1:-1]):
        k += 1
        up = (trees[i,k] > trees[:i,k])[::-1]
        down = (trees[i,k] > trees[i+1:,k])
        left=  (trees[i,k] > trees[i,:k])[::-1]
        right =  (trees[i,k] > trees[i,k+1:])



        up = sum(up[:np.argmin(up)])+1
        down = sum(down[:np.argmin(down)])+1
        left = sum(left[:np.argmin(left)])+1
        right = sum(right[:np.argmin(right)])+1


        print(up, left, down, right)

        max_score[i,k] = up * down * left * right

b = sns.heatmap(max_score)
plt.savefig("heatmap.pdf")

print(f"The best view score is {np.max(max_score)}")



