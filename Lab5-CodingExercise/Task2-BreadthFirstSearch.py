graph = {
    'A': ['B', 'F', 'D', 'E'],
    'B': ['K', 'J'],
    'K': ['N', 'M'],
    'J': [],
    'N': [],
    'M': [],
    'F': [],
    'D': ['G'],
    'G': [],
    'E': ['C', 'H', 'I'],
    'C': [],
    'H': [],
    'I': ['L'],
    'L': []
}

from collections import deque

def bfs(graph, start, goal):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        print("Visiting:", node)

        if node == goal:
            print("Goal node found:", node)
            return

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])

# Run BFS
bfs(graph, 'A', 'G')
