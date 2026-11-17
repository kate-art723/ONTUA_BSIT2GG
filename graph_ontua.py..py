
from collections import deque

# GRAPH - ONTUA

graph = {
    "O": ["N", "T"],
    "N": ["O", "U", "A"],
    "T": ["O", "A"],
    "U": ["N", "A"],
    "A": ["N", "T", "U"]
}


# Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)


# Depth-First Search (DFS)
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


# Display Results
print("GRAPH - ONTUA")

print("\nGraph BFS:")
bfs(graph, "O")

print("\n\nGraph DFS:")
print("DFS Traversal:", end=" ")
dfs(graph, "O", set())

print("\n")
