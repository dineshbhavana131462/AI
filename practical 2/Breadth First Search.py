
# Breadth First Search
def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()
    while queue:
