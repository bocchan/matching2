# -*- coding: utf-8 -*-
"""
http://skzy.hatenablog.com/entry/2013/01/26/050459
http://ja.wikipedia.org/wiki/%E5%AE%89%E5%AE%9A%E7%B5%90%E5%A9%9A%E5%95%8F%E9%A1%8C
http://toyokeizai.net/articles/-/11584?page=2
http://docs.python.jp/2/tutorial/datastructures.html
"""
def deferred_acceptance():

#M,Fのindexが男性の名前を表し、内包されているリストが選好を表します。
    M = [[2,1,0], [1,2,0], [1,0,2]]
    F = [[1,0,2], [1,0,2], [0,2,1]]
#Mの名前をただ定義します。
    single = [0, 1, 2]
#女性から見た相手のリストを仮に作ります。
    pair = [-1, -1, -1]




#アルゴリズムを実行します。
    while len(single)>0:
        x = single.pop()
        y = M[x].pop()
        if pair[y] != -1:
            if F[y].index(pair[y]) < F[y].index(x):
                single.insert(0, pair[y])
                pair[y] = x
            else:
                single.insert(0, x)
        else:
            pair[y] = x
        return pair
#ペア成立した組を表示します。(M,,F)の順
for i in pair :
    print (pair[i], i)