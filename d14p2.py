from template import *
p = ial("input.txt")
counts = dd(int)
keycounts = dd(int)
fmap = {}
rules = dict((a, b) for a, b in re.findall(r"(\w\w) -> (\w)", ias("input.txt")))
k = p[0]
for i in range(len(k)-2, -1, -1):
    ch = k[i] + k[i+1]
    if ch in rules:
        keycounts[ch] += 1
    counts[k[i+1]] += 1

counts[k[0]] += 1


for _ in range(40):
    for key in keycounts:
        counts[rules[key]] += keycounts[key]
    
    newkcount = dd(int)
    for key in keycounts:
        j = [key[0] + rules[key], rules[key] + key[1]]
        for key2 in j:
            if key2 in rules:
                newkcount[key2] += keycounts[key]
    keycounts = newkcount

    

g = list(counts.values())
print(max(g) - min(g))

