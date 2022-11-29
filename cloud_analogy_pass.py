n=[1,4,2,3,5,7]
m=n[::-1]
l=[]
print(m)

for i in range(len(m)-1):
    a=m[i]+m[i+1]
    l.append(a)
l.append(m[len(m)-1])
print(l)