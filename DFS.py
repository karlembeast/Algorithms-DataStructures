class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,node,vertex):
        if node not in self.graph:
            self.graph[node] = [vertex]
        else:
            self.graph[node].append(vertex)

    def check_adjacent_nodes(self,start,visited_nodes):
        visited_nodes[start] = [True]
        print(start)

        for i in self.graph[start]:
            if visited_nodes[i] == False:
                self.check_adjacent_nodes(i,visited_nodes)

    def DFS(self,start):
        visited_nodes = [False]*(len(self.graph))
        self.check_adjacent_nodes(start,visited_nodes)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Depth First Search:")
g.DFS(2)
