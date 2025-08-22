# Input number of nodes
n = int(input("Enter the number of nodes: ").strip())

# Initialize adjacency list
graph = [[] for _ in range(n)]

# Function to add an undirected edge
def addEdge(x, y):
    graph[x].append(y)
    graph[y].append(x)

# DFS function
def dfs(node, visited):
    visited[node] = True
    print(node, end=" ")  # Print node when visited
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)

# Input number of edges
m = int(input("Enter the number of edges: ").strip())

# Input edges
for _ in range(m):
    u, v = map(int, input("Enter edge (u v): ").split())
    addEdge(u, v)

# Initialize visited array
visited = [False] * n

# Start DFS from node 0 (or any node)
print("DFS Traversal starting from node 0:")
dfs(0, visited)
    
