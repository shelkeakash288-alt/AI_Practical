from collections import deque

grid = [
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

rows = len(grid)
cols = len(grid[0])

def find_path(start, goal):

    queue = deque([start])
    parent = {start: None}
    visited = {start}

    moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:

        current = queue.popleft()

        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        r, c = current

        for dr, dc in moves:

            nr = r + dr
            nc = c + dc

            nxt = (nr, nc)

            if (0 <= nr < rows and
                0 <= nc < cols and
                grid[nr][nc] == 0 and
                nxt not in visited):

                visited.add(nxt)
                parent[nxt] = current
                queue.append(nxt)

    return None

path = find_path(start, goal)

if path:
    print("Safe Path:")
    print(path)
else:
    print("No path exists")