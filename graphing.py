from collections import deque
class graph():

    def __init__(self, edges):
        assert(type(edges) == dict)
        self.graph = edges

    def bfs(self, startpoint, elem):
        q = [startpoint]
        searched = {startpoint}
        depth = 1
        while q:
            nq = []
            for node in q:
                for n in self.graph[node]:
                    if n in searched:
                        continue
                    if n == elem:
                        return (depth, True)
                    nq.append(n)
                    searched.add(n)
            q = nq
            depth += 1
        return (-1, False)




