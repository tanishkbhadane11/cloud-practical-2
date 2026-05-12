graph={'A':[('B',1),('C',2)],'B':[('D',1)],'C':[],'D':[]}

h={'A':3,'B':1,'C':1,'D':0}

start=input('Start: ')
goal=input('Goal: ')

open=[(start,0)]

while open:
    open.sort(key=lambda x:x[1])
    node,cost=open.pop(0)

    print(node,end=' ')

    if node==goal:
        break

    for i,w in graph[node]:
        open.append((i,w+h[i]))
