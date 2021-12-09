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

n = ["cagedb", "", "gcdfa", "fbcad", "", "cdfbe", "cdfgeb", "", "", "cgfabd"]
m = {2:1, 4:4, 3:7, 7:8}
c = 0
for line in ial("input.txt"):
    a, b = line.split("|")
    a = a.split()
    a.sort(key=len)
    a = a[:3]+[a[-1]]
    a = dict(zip([1, 7, 4, 8], a))
    print(a)

    b = b.split()
    op = ""
    for y in b:
        if len(y) in [2, 3, 4, 7]:
            op += str(m[len(y)])
        else:
            if len(y) == 5:
                if all(ch in y for ch in a[1]):
                    op += "3"
                else:
                    lo = [ch for ch in y if ch in a[4]]
                    if len(lo) == 2:
                        op += "2"
                    else:
                        op += "5"
            else:
                if all(ch in y for ch in a[4]):
                    op += "9"
                elif all(ch in y for ch in a[1]):
                    op += "0"
                else:
                    op += "6"
    c += int(op)
print(c)

