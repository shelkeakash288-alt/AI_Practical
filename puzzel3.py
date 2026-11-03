import heapq

GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def manhattan(state):

    distance = 0

    for index, tile in enumerate(state):

        if tile == 0:
            continue

        goal_index = tile - 1

        r1, c1 = divmod(index, 3)
        r2, c2 = divmod(goal_index, 3)

        distance += abs(r1-r2) + abs(c1-c2)

    return distance


def neighbors(state):

    blank = state.index(0)
    r, c = divmod(blank, 3)

    for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:

        nr = r + dr
        nc = c + dc

        if 0 <= nr < 3 and 0 <= nc < 3:

            new_blank = nr * 3 + nc

            board = list(state)

            board[blank], board[new_blank] = (
                board[new_blank], board[blank]
            )

            yield tuple(board)


def astar(start):

    pq = [(manhattan(start), 0, start)]

    parent = {start: None}
    best_g = {start: 0}

    while pq:

        f, g, state = heapq.heappop(pq)

        if state == GOAL:

            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        if g != best_g[state]:
            continue

        for nxt in neighbors(state):

            new_g = g + 1

            if new_g < best_g.get(nxt, float("inf")):

                best_g[nxt] = new_g
                parent[nxt] = state

                heapq.heappush(
                    pq,
                    (new_g + manhattan(nxt), new_g, nxt)
                )

    return None


start = tuple(map(int, input("Enter 9 numbers (0 for blank): ").split()))

if len(start) != 9 or set(start) != set(range(9)):
    print("Invalid input")

else:

    solution = astar(start)

    if solution:

        print("Moves:", len(solution) - 1)

        for step in solution:

            for i in range(0, 9, 3):
                print(step[i:i+3])

            print()

    else:
        print("No solution found")