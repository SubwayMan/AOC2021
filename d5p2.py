from typing import List
import re

def ias(filename:str = "input.txt") -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def ial(filename:str = "input.txt") -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return ias(filename).split("\n")

def iai(filename:str = "input.txt") -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = ial(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))

k = [[0 for i in range(2000)] for j in range(2000)]
edges = [(int(a), int(b), int(c), int(d)) for a, b, c, d in re.findall(r"(\d+),(\d+) -> (\d+),(\d+)", ias("input.txt"))]
for a, b, c, d in edges:
    print(a, b, c, d)
    if a==c:
        k1 = min(b, d)
        k2 = max(b, d)

        for i in range(k1, k2+1):

            k[i][a] += 1

    elif b==d:
        k1 = min(a, c)
        k2 = max(a, c)
        for i in range(k1, k2+1):
            k[b][i] += 1

    elif abs(c-a) == abs(d-b):
        a2, b2, c2, d2 = a, b, c, d 
        if a > c:
            c2, a2 = a, c
            b2, d2 = d, b
        
        ymod = 1
        if b2 > d2:
            ymod = -1
        for i in range(c2-a2+1):
            k[b2+(ymod*i)][a2+i] += 1
        




g = 0
for u in k:
    g += len([op for op in u if op >= 2])
print(g)

