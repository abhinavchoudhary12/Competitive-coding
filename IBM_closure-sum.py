def consom(n):
    s=str(n)
    l=len(s)
    result=0
    if l%2==0:
    
        for i in range(l//2):
            sum1=int(s[i])
            sum1*=10
            sum1=sum1+int(s[l-i-1])
            result+=sum1
        return result
    if l%2!=0:
        for i in range(l//2+1):
            sum1=int(s[i])
            sum1*=10
            sum1=sum1+int(s[l-1-i])
            #print(sum1)
            if i==l//2:
                sum1//=10
            result+=sum1
        return result
n=int(input())
print(consom(n))
            