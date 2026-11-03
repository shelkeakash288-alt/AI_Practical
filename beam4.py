import random

D = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def route_cost(route):

    total = 0

    for i in range(len(route)):
        total += D[route[i]][route[(i+1) % len(route)]]

    return total


def local_beam_search(k=3, iterations=100):

    n = len(D)
    beam = []

    while len(beam) < k:

        route = [0] + random.sample(range(1, n), n-1)

        if route not in beam:
            beam.append(route)

    for _ in range(iterations):

        candidates = set()

        for route in beam:

            for i in range(1, n):

                for j in range(i+1, n):

                    new_route = route[:]

                    new_route[i], new_route[j] = (
                        new_route[j], new_route[i]
                    )

                    candidates.add(tuple(new_route))

        if not candidates:
            break

        best = sorted(candidates, key=route_cost)

        beam = [list(r) for r in best[:k]]

    return min(beam, key=route_cost)


best_route = local_beam_search()

names = ["A", "B", "C", "D"]

tour = [names[i] for i in best_route]
tour.append(names[best_route[0]])

print("Best Tour:", " -> ".join(tour))
print("Total Distance:", route_cost(best_route))