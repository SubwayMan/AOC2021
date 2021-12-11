from template import *
ans = 0

refl = {")": 3, "]": 57, "}": 1197, ">": 25137}
remap = dict(zip("({[<", ")}]>"))
print(remap)
for line in ial("input.txt"):
    k = []
    for i in range(len(line)):
        if line[i] in ">)}]":
            p = k.pop(-1)
            if remap[p] != line[i]:
                print(p, line[i])
                h = line[i]
                ans += refl[h]
                break
        else:
            k.append(line[i])

print(ans)

