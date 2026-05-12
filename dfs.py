graph={}

n=int(input('Enter no of nodes: '))

for i in range(n):
    node=input('Node: ')
    neighbours=input('Neighbours: ').split()
    graph[node]=neighbours

start=input('Start node: ')

visited=set()

def dfs(node):
    if node not in visited:
        print(node,end=' ')
        visited.add(node)

        for i in graph[node]:
            dfs(i)

dfs(start)
