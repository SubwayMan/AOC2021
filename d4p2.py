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

ad = [*map(int, ial()[0].split(","))]
nxt = ias().rstrip().split("\n\n")[1:]
nxt = [k.split("\n") for k in nxt]
nxt = [[list(map(int, f.split())) for f in k] for k in nxt]
boards = [1 for pr in range(len(nxt))]


for card in ad:
    for b in range(len(nxt)):
        if boards[b] == 0:
            continue
        for row in range(len(nxt[b])):
            if card in nxt[b][row]:
                nxt[b][row] = [[i, -1][i==card] for i in nxt[b][row]]

        card2 = []
        for row2 in nxt[b]:
            card2 += row2

        if [-1]*5 in nxt[b] or tuple([-1]*5) in list(zip(*nxt[b])):
            boards[b] = 0
            if sum(boards) == 0:
                k = 0
                for elem in card2:
                    if elem != -1:
                        k += elem
                print(k*card)
                exit()


