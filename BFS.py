class Graph:
    def __init__(self):
        self.graph = {}

    def addEdge(self,node,vertex):
        if node not in self.graph:
            self.graph[node] = [vertex]
        else:
            self.graph[node].append(vertex)

    def BFS(self,start):
        visited_nodes = [False]*(len(self.graph))
        queue = []
        queue.append(start)
        visited_nodes[start] = True

        while queue:
            start = queue.pop(0)
            print(start)

            for i in self.graph[start]:
                if visited_nodes[i] == False:
                    queue.append(i)
                    visited_nodes[i] = True

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Breadth First Search:")
g.BFS(2)
