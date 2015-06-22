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