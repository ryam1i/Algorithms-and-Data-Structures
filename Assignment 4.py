from collections import deque

class Graph:
    def __init__(self, size):
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.size = size
        self.vertex_data = [''] * size  

    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1

    def add_vertex_data(self, vertex, data):
        self.vertex_data[vertex] = data

    def dfs_util(self, v, visited):
        visited[v] = True
        print(self.vertex_data[v], end=' ')
        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                self.dfs_util(i, visited)

    def dfs(self, start_node):
        visited = [False] * self.size
        self.dfs_util(self.vertex_data.index(start_node), visited)
        print()

    def bfs(self, start_node):
        visited = [False] * self.size
        queue = deque([self.vertex_data.index(start_node)])
        visited[self.vertex_data.index(start_node)] = True
        while queue:
            v = queue.popleft()
            print(self.vertex_data[v], end=' ')
            for i in range(self.size):
                if self.adj_matrix[v][i] == 1 and not visited[i]:
                    visited[i] = True
                    queue.append(i)
        print()

g = Graph(7)
nodes = ['A', 'C', 'B', 'D', 'E', 'G', 'F']
for i, name in enumerate(nodes):
    g.add_vertex_data(i, name)

edges = [(0,1), (0,2), (0,3), (2,1), (2,4), (2,5), (1,3), (4,5), (4,6), (6,5)]
for u, v in edges:
    g.add_edge(u, v)

print("DFS Result:")
g.dfs('A')
print("BFS Result:")
g.bfs('A')