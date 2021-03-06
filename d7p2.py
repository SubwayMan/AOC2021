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

k = [*map(int, ias("input.txt").split(","))]
op2 = (sum(k) // len(k))
j =[]
def tsum(k):
    return (k*(k+1))//2

for op in range(min(k), max(k)):
    j.append(sum(tsum(abs(i-op)) for i in k))

print(min(j))
