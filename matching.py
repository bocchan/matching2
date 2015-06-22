def deferred_acceptance(prop_prefs, resp_prefs):
    
    prop_num = len(prop_prefs)
    resp_num = len(resp_prefs)
    single = range(prop_num)
    prop_unmatched = resp_num
    resp_unmatched = prop_num
    
    prop_matched = [prop_unmatched for w in range(prop_num)]
    resp_matched = [resp_unmatched for z in range(resp_num)]
    
    counter = [0 for p in range(prop_num)]
    
    while len(single)>0:
        x = single.pop(0)
        y = prop_prefs[x][counter[x]]
        if y != prop_unmatched:
            if resp_matched[y] == resp_unmatched:
                if resp_prefs[y].index(resp_unmatched) > resp_prefs[y].index(x):
                    resp_matched[y] = x
                    prop_matched[x] = y
                else:
                    single.insert(0, x)
                    counter[x] += 1
            else:
                if resp_prefs[y].index(resp_matched[y]) > resp_prefs[y].index(x):
                    single.insert(0, resp_matched[y])
                    prop_matched[resp_matched[y]] = prop_unmatched
                    resp_matched[y] = x
                    prop_matched[x] = y
               
                else:
                    single.insert(0, x)
                    counter[x] += 1
    
    
    return prop_matched, resp_matched