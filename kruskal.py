edges=[]

n=int(input('Enter number of edges: '))

for i in range(n):
    u=input('Enter first node: ')
    v=input('Enter second node: ')
    w=int(input('Enter weight: '))

    edges.append((u,v,w))

edges.sort(key=lambda x:x[2])

parent={}

for u,v,w in edges:
    parent[u]=u
    parent[v]=v

def find(x):
    while parent[x]!=x:
        x=parent[x]
    return x

for u,v,w in edges:
    a=find(u)
    b=find(v)

    if a!=b:
        print(u,v,w)
        parent[a]=b
