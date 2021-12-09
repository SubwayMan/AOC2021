
k = open("input.txt", "r").read().rstrip().split("\n")
k = list(map(int, k))
c=0
for i in range(1, len(k)):
    if k[i] > k[i-1]:
        c+=1

print(c)
