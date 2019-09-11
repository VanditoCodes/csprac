f1=open('faiily1.txt','w+')
f = [["ucks ym ahd naigg"],["ten ten ent ent"],["hello guys lala upl iopl idky eef"]]

def isvowel():
    vwl = ['a','e','i','o','u']
    for i in f:
        for j in i[0].split():
            if any(l == j[0] for l in vwl):
                print(j)
                continue


a = isvowel()