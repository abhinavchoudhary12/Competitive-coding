inp=int(input("enter thr number of rows"))
a=[[0 for x in range(inp)]for y in range(inp)] 

for i in range(inp):
    for y in range(inp):
        print(a[i][y],end="")
    print("\n")
def isSafe(a,s,e,n):
    row=s
    col=e
    for i in range(row):
        if a[i][col]==1:
            return False
    row=s
    col=e
    while row>=0  and col>=0:
        if a[row][col]==1:
            return False
        row-=1
        col-=1
    row=s
    col=e
    while row>=0 and col<n:
        if a[row][col]==1:
            return False
        row-=1
        col+=1
    return True
def nQueen(a,s,n):
    if s>=n:
        return True
    for i in range(n):
        if isSafe(a,s,i,n):
            a[s][i]=1
            if nQueen(a,s+1,n):
                return True
            a[s][i]=0
    return False
print("after n queen")
nQueen(a,0,inp)     
for i in range(inp):
    for j in range(inp):
        print(a[i][j],end="")
    print("\n")
