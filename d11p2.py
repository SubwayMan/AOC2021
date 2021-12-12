from template import *

octi = [list(map(int, f)) for f in ias("input.txt").split("\n")]

def adjac(r, c):
    for r2 in (r-1, r, r+1):
        for c2 in (c-1, c, c+1):
            if 0<=r2<len(octi) and 0<=c2<len(octi[0]) and (r2, c2) != (r, c):
                yield (r2, c2)
fl = 0

def flash(row, col):
    global fl
    octi[row][col] = 0
    for r, c in adjac(row, col):
        if octi[r][c] == 0:
            continue
        octi[r][c] += 1
        if octi[r][c] > 9:
            octi[r][c] = 0
            flash(r, c)
    fl += 1

p = 0
while True:
    p += 1

    octi = [[i+1 for i in octi[r]] for r in range(len(octi))]
    for row in range(len(octi)):
        for col in range(len(octi[0])):
            if octi[row][col] >9:
                flash(row, col)

    for rr in octi:
        if not all(x==0 for x in rr):
            break
    else:
        print(p)
        break

