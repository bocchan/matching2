def deferred_acceptance(prop_prefs, resp_prefs, caps=None):
    
    if caps == None:
        caps = [1 for i in list(range(len(resp_prefs)))]

    caps_cntr = list(caps)
    
    prop_num = len(prop_prefs)
    resp_num = len(resp_prefs)
    single = list(range(prop_num))
    prop_unmatched = resp_num
    resp_unmatched = prop_num

    prop_matched = [prop_unmatched for j in list(range(prop_num))]
    resp_matched = [resp_unmatched for k in list(range(sum(caps)))]
    counter = [0 for l in list(range(prop_num))]

    while len(single)>0:
        x = single.pop(0)
        print x
        print counter
        y = prop_prefs[x][counter[x]]
        if y != prop_unmatched:
            if caps_cntr[y] > 1:
                if y == 0:
                    resp_matched[caps_cntr[y]-1] = x
                    prop_matched[x] = y
                    caps_cntr[y] = caps_cntr[y] - 1
                if y > 0:
                    now_y = cumsum(caps, y-1) + caps_cntr - 2
                    resp_matched[now_y] = x
                    prop_matched[x] = y
                    caps_cntr[y] = caps_cntr[y] - 1
            else:
                if resp_matched[y] == resp_unmatched:
                    if resp_prefs[y].index(resp_unmatched) > resp_prefs[y].index(x):
                        if y == 0:
                            args_y = caps[y] - 1
                        else:
                            args_y = cumsum(caps, y-1) - 1
                        resp_matched[args_y] = x
                        prop_matched[x] = y
                    else:
                        single.insert(0, x)
                        counter[x] += 1
                else:
                    m = caps[y]
                    pooled = []
                    while m > 0:
                        pooled_psn = resp_matched[cumsum(caps, y) - caps[y] + m -1]
                        pooled.append(pooled_psn)
                        m = m - 1
                    pooled_index = []
                    for n in pooled:
                        pooled_index.append(resp_prefs[y].index(n))
                    worst = max(pooled_index)
                    worst_psn = resp_prefs[y][worst]
                    
                    if x != worst_psn:
                        if worst_psn != resp_unmatched:
                            single.insert(0, worst_psn)
                            prop_matched[worst_psn] = prop_unmatched
                            resp_matched[resp_matched.index(worst_psn)] = x
                            prop_matched[x] = y
                            counter[worst_psn] += 1
                        else:
                            prop_matched[x] = y
                            
                    else:
                        single.insert(0, x)
                        counter[x] += 1

    return prop_matched, resp_matched
