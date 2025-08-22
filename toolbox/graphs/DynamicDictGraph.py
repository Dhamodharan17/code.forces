# Initialize empty graph
graph = {}

# Function to add a node
def addNode(node):
    if node not in graph:
        graph[node] = []

# Function to add an edge (undirected)
def addEdge(u, v):
    addNode(u)
    addNode(v)
    graph[u].append(v)
    graph[v].append(u)

# DFS function
def dfs(node, visited):
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# Example usage
# Add nodes and edges
addEdge(0, 1)
addEdge(0, 2)
addEdge(1, 3)
addEdge(3, 4)

# Add a new node dynamically
addNode(5)
addEdge(4, 5)

# Perform DFS starting from node 0
visited = set()
print("DFS Traversal starting from node 0:")
dfs(0, visited)
