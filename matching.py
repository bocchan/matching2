import copy
import numpy as np

m_prefs=np.array([[4,0,1,2,3],[1,2,0,3,4],[3,1,0,2,4]])
f_prefs=np.array([[0,1,2,3],[1,0,3,2],[1,2,0,3],[0,3,2,1]])

def array_to_dict(array):
    dict = {}
    for x, y in enumerate(array):
        dict[x] = list(y)
    return dict

  
def deferred_acceptance(m_prefs,f_prefs):
    m_prefers = array_to_dict(m_prefs)
    f_prefers = array_to_dict(f_prefs)
    guys = sorted(m_prefers.keys())
    gals = sorted(f_prefers.keys())
    guysfree = guys[:]
    engaged  = {}
    guyprefers2 = copy.deepcopy(m_prefers)
    galprefers2 = copy.deepcopy(f_prefers)
    while guysfree:
        guy = guysfree.pop(0)
        guyslist = guyprefers2[guy]
        gal = guyslist.pop(0)
        fiance = engaged.get(gal)
        if not fiance:
            # She's free
            engaged[gal] = guy
        else:
            # The bounder proposes to an engaged lass!
            galslist = galprefers2[gal]
            if galslist.index(fiance) > galslist.index(guy):
                # She prefers new guy
                engaged[gal] = guy
                if guyprefers2[fiance]:
                    # Ex has more girls to try
                    guysfree.append(fiance)
            else:
                # She is faithful to old fiance
                if guyslist:
                    # Look again
                    guysfree.append(guy)
    return engaged
 
print engaged #女性、男性の順