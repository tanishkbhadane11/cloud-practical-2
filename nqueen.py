n=int(input('Enter N: '))

x=[]

def safe(r,c):
    for i,j in x:
        if j==c or abs(i-r)==abs(j-c):
            return False
    return True

def solve(r):
    if r==n:
        print(x)
        return

    for c in range(n):
        if safe(r,c):
            x.append((r,c))
            solve(r+1)
            x.pop()

solve(0)
