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
    def dfs(graph):
        