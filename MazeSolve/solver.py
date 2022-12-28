from pyamaze import maze

class graph:
    def generateGraph(map: dict):
        graph = {}
        for item in map:
            graph[item] = list()
            for connected in map[item]:
                if map[item][connected] == 1:
                    if connected == 'E':
                        key = item[0], item[1]+1
                    elif connected == 'W':
                        key = item[0], item[1]-1
                    elif connected == 'S':
                        key = item[0]+1, item[1]
                    elif connected == 'N':
                        key = item[0]-1, item[1]
                    graph[item].append(key)
        return graph

class solver:
    path = []
    cPath = []

    def dfsCaller(graph, start, end):
        solver.path = []
        solver.dfs([], graph, start, end)
        solver.path.reverse()
        return solver.path
    
    def dfs(visited:list, graph, node, end):
        if node not in visited:
            solver.cPath.append(node)
            visited.append(node)
            if node == end:
                solver.path.append(node)
                return True
            else:
                for connected in graph[node]:
                    if solver.dfs(visited, graph, connected, end):
                        solver.path.append(node)
                        return True
                return False
