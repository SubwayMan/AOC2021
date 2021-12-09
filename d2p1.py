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

k = ial()

x = 0
y = 0

for i in k:
    c, n = i.split()

    if c[0] in "ud":
        if c[0] == "u":
            y += int(n)
        else:
            y-=int(n)

    else:
        if c[0] == "f":
            x += int(n)

        else:
            x-= int(n)

print(y*x)
