def find_AllEdge(graphs):
    ListEdge = []
    for keys in graphs.keys():
        if graphs[keys] != []:
            for value in graphs[keys]:
                temp = keys+' => '+value,
                ListEdge.append(temp)
    return ListEdge

def all_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not start in graph:
        return []
    paths = []
    for node in graph[start]:
        if not node in path:
            newpaths = all_path(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not start in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_ListShortestPath(Allpaths,ShortestPath):
    ListShortest = [];
    for path in Allpaths:
        if len(path) == len(ShortPath):
            ListShortest.append(path)
    return ListShortest

def displayBlock(Paths):
    for i in range(len(Paths)):
         print('Path',i+1,'=',Paths[i])

g = {
    'A': ['B','C','D'],
    'B': ['C','e','F'],
    'C': ['F'],
    'D': ['C','G','T'],
    'E': ['T'],
    'F': ['T'],
    'G': ['T'],
    'T': []
    }

SemuaEdge = find_AllEdge(g)
print('\nBanyaknya Edge : ')
displayBlock(SemuaEdge)

ListAll_Path = all_path(g,'A','T')
print('\nBanyaknya Path : ')
displayBlock(ListAll_Path)

ShortPath = shortest_path(g,'A','T')
ListShortestPath = find_ListShortestPath(ListAll_Path,ShortPath)
print('\nPath Terpendek : ')
displayBlock(ListShortestPath)