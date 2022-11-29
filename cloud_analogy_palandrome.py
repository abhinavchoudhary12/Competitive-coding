def pal(n):
    m=n[::-1]
    if m==n:
        return 1
    else:
        return 0
n=input()
count=""
for i in range(len(n)):
    l=""
    count=n[i]
    for j in range(len(n)):
        if j !=i:
            l+=n[j]
    if pal(l):
        print(count)
        break