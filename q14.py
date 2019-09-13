f = open('q1412th.txt','r+')
f.seek(0)
l = f.readlines()
g = []
f.seek(0)

for i in range(0,len(l)):
    x = (l)[i].rstrip('\n')
    g.append(tuple(x.split('\t')))
    
    
print(g)
