from template import *
import graphing

gr = dd(list)
starts = []
ends = []
smap = {}
for line in ial("input.txt"):
    n, com = line.split("-")
    
    gr[com].append(n)
    gr[n].append(com)
    for f in [n, com]:
        if f.islower():
            smap[f] = False

smap["start"]=True

print(gr)
paths = set()
allt = 0
def dfs(node, smap, pr):
    global allt
    #print(node, smap)
    pr += node + ","
    tot = 0
    for n in gr[node]:
        if n == "end":
            allt += 1
            paths.add(pr)
            print(pr)
        elif n.islower():
            if not smap[n]:
                smap2 = smap.copy()
                smap2[n] = True
                tot += dfs(n, smap2, pr)
        else:
            tot += dfs(n, smap, pr)
    return tot

ans = 0
dfs("start", smap, "")

print(allt)
print(len(paths))




