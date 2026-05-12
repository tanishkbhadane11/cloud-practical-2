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

selected=[start]

while len(selected)<len(graph):
    m=999

    for i in selected:
        for j in graph[i]:
            if j not in selected and graph[i][j]<m:
                m=graph[i][j]
                a=j

    print(a,m)
    selected.append(a)
