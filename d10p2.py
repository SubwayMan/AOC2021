from template import *
ans = []

refl = {")": 1, "]": 2, "}": 3, ">": 4}
remap = dict(zip("({[<", ")}]>"))
print(remap)
for line in ial("input.txt"):
    k = []
    for i in range(len(line)):
        if line[i] in ">)}]":
            p = k.pop(-1)
            if remap[p] != line[i]:
                h = line[i]
                break
        else:
            k.append(line[i])
    else:
        poi = 0
        for i in k[::-1]:
            poi *= 5
            poi += refl[remap[i]]

        ans.append(poi)
ans.sort()
print(ans)
print(ans[len(ans)//2])

