from template import *
import graphing
import sys
sys.setrecursionlimit(100000)
gr = dd(list)
starts = []
ends = []
smap = {}
ref = set(ial("input4.txt"))
for line in ial("input.txt"):
    n, com = line.split("-")
    
    gr[com].append(n)
    gr[n].append(com)
    for f in [n, com]:
        if f.islower():
            smap[f] = 0

smap["start"]=2

print(gr)
paths = set()
allt = 0

def dfs(node, smap, pr, fl):
    global allt
    #print(node, smap)
    pr += node + ","
    tot = 0
    for n in gr[node]:
        if n == "end":
            allt += 1
            pr += "end"
            paths.add(pr)

        elif n.islower():
            if smap[n] == 0:
                smap2 = smap.copy()
                smap2[n] += 1
                tot += dfs(n, smap2, pr, fl)

            elif smap[n] == 1 and fl:
                tot += dfs(n, smap, pr, False)
        else:
            tot += dfs(n, smap, pr, fl)
    return tot

ans = 0
dfs("start", smap, "", True)
print(len(paths))




