from template import *
p = ial("input.txt")
k = list(p[0])
rules = dict((a, b) for a, b in re.findall(r"(\w\w) -> (\w)", ias("input.txt")))
for i in range(10):
    for i in range(len(k)-2, -1, -1):
        if k[i] + k[i+1] in rules:
            k.insert(i+1, rules[k[i]+k[i+1]])
    

f = sorted([k.count(a) for a in set(k)])
print(f[-1] - f[0])

