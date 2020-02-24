class Solution:
        def isBipartite(self, graph: List[List[int]]) -> bool:
            VertColor = len(graph) * [0]
            visited = len(graph) * [False]
            VertColor[0] = 1
            for i in range(len(graph)):
                if(not visited[i]):
                    visited[i] = True
                    VertColor[i] = 1
                    visitQ = [i] 
                    while (visitQ):
                        x = visitQ.pop(0)
                        for ver in graph[x]:
                            if(visited[ver] and VertColor[ver] == VertColor[x]):
                                return False
                            if(not visited[ver]):
                                VertColor[ver] = -1*VertColor[x]
                                visited[ver] = True
                                visitQ.append(ver)
            return True
