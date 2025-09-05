from collections import defaultdict


def roc_loss(ys, ps):
    t = zip(ys, ps)
    sorted_t = sorted(t, key=lambda x: -x[1])
    roc = []
    i = 0
    while True:
        counts = defaultdict(int)
        counts[sorted_t[i][0]] += 1
        total = 1
        if i < len(sorted_t) - 1:
            for j in range(i + 1, len(ys)):
                if sorted_t[i][1] != sorted_t[j][1]:
                    break
                counts[sorted_t[j][0]] += 1
                total += 1

        if len(counts.keys()) > 1:
            roc.append([1, 1] if len(roc) == 0 else [roc[-1][0] + 1, roc[-1][1] + 1])
        else:
            if sorted_t[i][0] == 0:
                roc.append([0, 1] if len(roc) == 0 else [roc[-1][0], roc[-1][1] + 1])
            else:
                roc.append([1, 0] if len(roc) == 0 else [roc[-1][0] + 1, roc[-1][1]])

        i += total
        if i >= len(ys):
            break

    return roc

def roc_auc_score(ys, ps):
    roc = roc_loss(ys, ps)
    r = 0
    last_x, last_y = 0, 0
    for y, x in roc:
        if x != last_x:
            r += y if y == last_y else y - 0.5

        last_x = x
        last_y = y

    return r / (roc[-1][0] * roc[-1][1])