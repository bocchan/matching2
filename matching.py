import numpy as np


def deferred_acceptance(prop_prefs, resp_prefs, caps=None):

    prop_num = len(prop_prefs)
    resp_num = len(resp_prefs)

    if caps is None:
        indptr = np.arange(resp_num+1)
        caps_cp = [1 for h in list(range(len(resp_prefs)))]
    else:
        indptr = np.empty(resp_num+1, dtype=int)
        indptr[0] = 0
        np.cumsum(caps, out=indptr[1:])
        caps_cp = caps

    caps_cntr = list(caps_cp)

    single = list(range(prop_num))
    prop_unmatched = resp_num
    resp_unmatched = prop_num

    prop_matched = [prop_unmatched for j in list(range(prop_num))]
    resp_matched = [resp_unmatched for k in list(range(sum(caps_cp)))]
    counter = [0 for l in list(range(prop_num))]

    while len(single) > 0:
        x = single.pop(0)
        y = prop_prefs[x][counter[x]]
        if y != prop_unmatched:
            if caps_cntr[y] >= 1:
                if resp_prefs[y].index(resp_unmatched) > resp_prefs[y].index(x):
                    now_y = sum(caps_cp[:y]) + caps_cntr[y] - 1
                    resp_matched[now_y] = x
                    prop_matched[x] = y
                    caps_cntr[y] = caps_cntr[y] - 1
                else:
                    single.insert(0, x)
                    counter[x] += 1
            else:
                m = caps_cp[y]
                pooled = resp_matched[indptr[y]:indptr[y+1]]
                pooled_index = []
                for n in pooled:
                    pooled_index.append(resp_prefs[y].index(n))
                worst = max(pooled_index)
                worst_psn = resp_prefs[y][worst]

                if resp_prefs[y].index(worst_psn) > resp_prefs[y].index(x):
                    single.insert(0, worst_psn)
                    prop_matched[worst_psn] = prop_unmatched
                    resp_matched[resp_matched.index(worst_psn)] = x
                    prop_matched[x] = y
                    counter[worst_psn] += 1
                else:
                    single.insert(0, x)
                    counter[x] += 1

    if caps is None:
        return prop_matched, resp_matched
    else:
        return prop_matched, resp_matched, indptr
