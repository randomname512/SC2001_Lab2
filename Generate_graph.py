import json
import random


def random_exclude(start, end, exclude, num):
    out = []
    while len(out) != num:
        curr = random.randint(start, end)
        if curr not in exclude:
            out.append(curr)
            exclude.append(curr)
    return out


# v = number of vertices
# e = number of edges per vertex
# n = number of graph to generate
def generate_graph(v, e, n=5):
    weight_max = 100
    for i in range(n):
        graph = {"v": v}
        for i2 in range(v):
            # guarantee path double weight to make it less likely for path to be 1,2,3 etc.
            graph[i2] = {(i2 + 1) % v: random.randint(1, weight_max * 2)}
            for i3 in random_exclude(0, v - 1, [i2, (i2 + 1) % v], e - 1):
                graph[i2][i3] = random.randint(1, weight_max)
        with open(f"data/{v}_{e}_{i}.json", "w") as file:
            json.dump(graph, file)
