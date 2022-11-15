n=int(input())
result=1
for i in range(1,n+1):
    result*=i**(n-i+1)
    
print(result)