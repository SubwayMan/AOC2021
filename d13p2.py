from template import *
k = [(int(a), int(b)) for a, b in re.findall(r"(\d+),(\d+)", ias("input.txt"))]
folds = [(ch, int(n)) for ch, n in re.findall(r"fold along (y|x)=(\d+)", ias("input.txt"))]

points = set(k)
for orient, val in folds:
    npoints = set()
    for a, b in points:
        if orient == "x" and a > val:
            npoints.add((val - (a-val), b))
        elif orient == "y" and b > val:
            npoints.add((a, val - (b-val)))
        else:
            npoints.add((a, b))
    points = npoints.copy()

k = [["." for i in range(50)] for j in range(10)]
for x, y in points:
    k[y][x] = "#"
for row in k:
    print(" ".join(row))

