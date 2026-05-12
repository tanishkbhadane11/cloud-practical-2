graph={}

n=int(input('Enter no of nodes: '))

for i in range(n):
    node=input('Enter node: ')
    m=int(input('Enter neighbour count: '))
    temp={}

    for j in range(m):
        nb=input('Enter neighbour: ')
        w=int(input('Enter weight: '))
        temp[nb]=w

    graph[node]=temp

start=input('Enter start node: ')

dist={}

for i in graph:
    dist[i]=999

dist[start]=0

for n in graph:
    for i in graph[n]:
        dist[i]=min(dist[i],dist[n]+graph[n][i])

print(dist)
