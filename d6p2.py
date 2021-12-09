from typing import List
from collections import defaultdict as dd
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

ints = [*map(int, ias("input.txt").split(","))]
print(ias())

p = [0 for i in range(9)]
for i in ints:
    p[i] += 1

for i in range(256):

    
    
    k = [0 for i in range(9)]

    for i in range(7):
        k[(i-1)%7] += p[i]

    k[7] = p[8]
    k[8] = k[6]
    k[6] += p[7]
    p = k


print(sum(p))

