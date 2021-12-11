from template import *

p = ial("input.txt")

seen = [[-1 for i in range(len(p[0]))] for j in range(len(p))]
def adjac(r, c):
    adj =[]
    if r < len(p)-1:
        adj.append((r+1, c))
    if r > 0:
        adj.append((r-1, c))
    if c < len(p[0])-1:
        adj.append((r, c+1))
    if c > 0:
        adj.append((r, c-1))
    
    k = []
    for r2, c2 in adj:
        if p[r2][c2] != "9":
            k.append((r2, c2))
    return k

def bfs(r, c):
    if seen[r][c] == 1:
        return 0

    q = deque([(r, c)])
    seen[r][c] = 1
    if p[r][c] == 9:
        return 0
    ans = 0
    while q:
        r3, c3 = q.popleft()
        adjh = adjac(r3, c3)
        for i, j in adjh:
            if seen[i][j] == -1:
                q.append((i, j))
                seen[i][j] = 1
                ans += 1

    return ans

f = []
for r in range(len(p)):
    for col in range(len(p[0])):
        f.append(bfs(r, col))
f.sort(reverse=True)
print(f[0]*f[1]*f[2])
