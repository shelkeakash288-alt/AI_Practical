def next_states(state, cap_a, cap_b):

    a, b = state

    return {
        (cap_a, b),
        (a, cap_b),
        (0, b),
        (a, 0),

        (a-min(a, cap_b-b),
         b+min(a, cap_b-b)),

        (a+min(b, cap_a-a),
         b-min(b, cap_a-a))
    }


def dfs_water_jug(cap_a, cap_b, target):

    start = (0, 0)

    stack = [start]

    parent = {start: None}

    while stack:

        state = stack.pop()

        a, b = state

        if a == target or b == target:

            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        for nxt in next_states(state, cap_a, cap_b):

            if nxt not in parent:

                parent[nxt] = (a, b)
                stack.append(nxt)

    return None


solution = dfs_water_jug(4, 3, 2)

if solution:

    print("Water Jug Solution:")

    for state in solution:
        print(state)

else:
    print("Target not reachable")