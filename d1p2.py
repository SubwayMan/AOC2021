from typing import List


def input_as_string(filename:str = "input.txt") -> str:
    """returns the content of the input file as a string"""
    with open(filename) as f:
        return f.read().rstrip("\n")

def input_as_lines(filename:str = "input.txt") -> List[str]:
    """Return a list where each line in the input file is an element of the list"""
    return input_as_string(filename).split("\n")

def input_as_ints(filename:str = "input.txt") -> List[int]:
    """Return a list where each line in the input file is an element of the list, converted into an integer"""
    lines = input_as_lines(filename)
    line_as_int = lambda l: int(l.rstrip('\n'))
    return list(map(line_as_int, lines))


k = input_as_ints()
c=0
for i in range(4, len(k)+1):
    if sum(k[i-3:i]) > sum(k[i-4:i-1]):
        c+=1

print(c)
