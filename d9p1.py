from typing import List
import re
from collections import defaultdict as dd, Counter as coun, deque

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

p = ial("input2.txt")

def adjac(r, c):
    adj =[]
    if r < len(p)-1:
        adj.append((r+1, c))
    if r > 0:
        adj.append((r-1, c))
    if c < len(p[0])-1:
        adj.append((r, c+1))
    if c > 0:
        adj.append((r, c-1))
    
    y = int(p[r][c])
    k = []
    for r2, c2 in adj:
        k.append(int(p[r2][c2]))
    if all(i>y for i in k):
        print(r, c)
        return y + 1
    return 0

c = 0
for r in range(len(p)):
    for col in range(len(p[0])):
        c += adjac(r, col)

print(c)
