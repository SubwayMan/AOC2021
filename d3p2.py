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

l1 = dat.copy()
l2 = dat.copy()

for i in range(len(dat[0])):
    
    k1 = "".join(l1[p][i] for p in range(len(l1)))
    k2 = "".join(l2[p][i] for p in range(len(l2)))

    if len(l1) > 1:
        if k1.count("0") > k1.count("1"):
            for pl in l1.copy():
                if pl[i] == "1":
                    l1.remove(pl)

        else:
            for pl in l1.copy():
                if pl[i] == "0":
                    l1.remove(pl)
    if len(l2) > 1:
        if k2.count("0") > k2.count("1"):
            for pl in l2.copy():
                if pl[i] == "0":
                    l2.remove(pl)

        else:
            for pl in l2.copy():
                if pl[i] == "1":
                    l2.remove(pl)


print(int(l1[0], 2)*int(l2[0], 2))
