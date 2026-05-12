from collections import deque

graph={}

n=int(input('Enter no of nodes: '))

for i in range(n):
    node=input('Node: ')
    neighbours=input('Neighbours: ').split()
    graph[node]=neighbours

start=input('Start node: ')

visited=set()
queue=deque([start])

while queue:
    node=queue.popleft()

    if node not in visited:
        print(node,end=' ')
        visited.add(node)

        for i in graph[node]:
            queue.append(i)
