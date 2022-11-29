n=int(input())
m=list(map(int,input().split()))
def freq(n):
    l=[]
    n=str(n)
    [l.append(int(i)) for i in n]
    freq=[0 for i in range(max(l)+1)]
    for i in l:
        freq[i]+=1

    for i in freq:
        if i !=0:
            c=i
    for i in freq:
        if i!=0:
            if i!=c:
                return 0
    return 1
    
stable=[]
unstable=[]
for i in range(n):
    if freq(m[i]):
        stable.append(m[i])
    else:
        unstable.append(m[i])
print(sum(stable)-sum(unstable))