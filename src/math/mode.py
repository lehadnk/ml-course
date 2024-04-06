def mode(vector: list):
    map = dict()
    for v in vector:
        if (v not in map):
            map[v] = 1
        else:
            map[v] += 1

    max_v = 0
    max_k = 0
    for (k, v) in map.items():
        if v > max_v:
            max_v = v
            max_k = k

    return max_k
