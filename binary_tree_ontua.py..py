
from collections import deque

# BINARY TREE - ONTUA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create Binary Tree
root = Node("O")
root.left = Node("N")
root.right = Node("T")
root.left.left = Node("U")
root.left.right = Node("A")


# Breadth-First Search (BFS)
def bfs(root):
    if root is None:
        return

    queue = deque([root])

    print("BFS Traversal:", end=" ")

    while queue:
        current = queue.popleft()
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Depth-First Search (DFS)
def dfs(root):
    if root is None:
        return

    print(root.data, end=" ")
    dfs(root.left)
    dfs(root.right)


# Display Results
print("BINARY TREE - ONTUA")
print("\nBinary Tree BFS:")
bfs(root)

print("\n\nBinary Tree DFS:")
print("DFS Traversal:", end=" ")
dfs(root)

print("\n")
