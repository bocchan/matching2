<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
http://skzy.hatenablog.com/entry/2013/01/26/050459
http://ja.wikipedia.org/wiki/%E5%AE%89%E5%AE%9A%E7%B5%90%E5%A9%9A%E5%95%8F%E9%A1%8C
http://toyokeizai.net/articles/-/11584?page=2
http://docs.python.jp/2/tutorial/datastructures.html
"""
def deferred_acceptance(arg1, arg2):
    #受け取るデータはself.m_prefsとself.f_prefs
    single = range(len(arg1))
    print single
    for i in range(len(arg1)):
        arg1[i].reverse()
    
    arg1_matched = [len(arg2) for w in arg1]
    print arg1_matched
    arg2_matched = [len(arg1) for z in arg2]
    print arg2_matched
    while len(single)>0:
        x = single.pop()
        y = arg1[x].pop()
        if arg1_matched[y] == len(arg2):
            arg1_matched[y] = x
        else:
            if arg2[y].index(arg2_matched[y])<arg2[y].index(x):
                single.insert(0, x)
            else:
                single.insert(0, arg2_matched[y])
                arg2_matched[y] = x
     
    
    
    return arg1_matched, arg2_matched
=======
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
>>>>>>> b6eaed2016ddb61dae21ece90cf44081f14d7b02
