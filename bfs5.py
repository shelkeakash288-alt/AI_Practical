from collections import deque

grid = [
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)
goal = (3, 3)

R = len(grid)
C = len(grid[0])

def bfs(start, goal):

    queue = deque([start])

    parent = {start: None}

    directions = [
        (1, 0), (-1, 0),
        (0, 1), (0, -1)
    ]

    while queue:

        r, c = queue.popleft()
        current = (r, c)

        if current == goal:

            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            return path[::-1]

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            nxt = (nr, nc)

            if (0 <= nr < R and
                0 <= nc < C and
                grid[nr][nc] == 0 and
                nxt not in parent):

                parent[nxt] = (r, c)
                queue.append(nxt)

    return None


path = bfs(start, goal)

if path:
    print("Path:", path)
    print("Minimum Moves:", len(path)-1)

else:
    print("Goal cannot be reached")