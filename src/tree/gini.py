from collections import Counter

def gini_impurity(v1, v2):
    v1_counter = Counter(v1)
    v1_ginis = {k:v / len(v1) for k, v in v1_counter.items()}
    for v1v, v1cnt in v1_counter.items():
        v1_indices = [i for i, x in enumerate(v1) if x == v1v]
        v2_values = [v2[i] for i in v1_indices]

        v2_counter = Counter(v2_values)
        if len(v2_counter.items()) == 1:
            # There's no uncertainity if there's only one v1v + v2v pair, therefore impurity turns 0 for this particular v1v
            v1_ginis[v1v] = 0
            continue

        for v2v, v2cnt in v2_counter.items():
            v1_ginis[v1v] *= v2cnt / len(v2_values)

    return sum(v1_ginis.values())