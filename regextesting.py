
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

# (dir, x0, y0, mag, man)
def wire_intersect(w1, w2):
    dir1, x1, y1, mag1, man1 = w1
    dir2, x2, y2, mag2, man2 = w2

    if (dir1 in "UD" and dir2 in "UD"):
        if 
all_data = ias()
w1, w2 = all_data.split("\n")
d1 = [(a, int(b)) for a, b in re.findall(r"([UDLR])(\d+)", w1)]
d2 = [(a, int(b)) for a, b in re.findall(r"([UDLR])(\d+)", w2)]



x, y = 0, 0
maxpx = maxpy = minpx = minpy = 0

