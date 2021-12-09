from typing import List

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

dat = ial("input.txt")

c = ""
d = ""
for i in range(len(dat[0])):
    k = "".join(dat[p][i] for p in range(len(dat)))
    if k.count("0") > k.count("1"):
        c += "0"
        d += "1"
    else:
        c += "1"
        d += "0"

e = int(c, 2)
f = int(d, 2)
print(e*f)

