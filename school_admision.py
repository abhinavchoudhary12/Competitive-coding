
n=input()
no=[]
value=[]
for i in range(len(n)):
    if n[i] in ['1','2','3','4','5','6','7','8','9']:
        no.append(int(n[i]))
        if i !=len(n)-1:
            value.append(' ')
    else:
        value.append(n[i])
value=''.join(value)

value=value.split(' ')
for i in range(len(no)):
    for j in range (len(no)-1):
        if (no[j]>no[j+1]):
            temp=no[j]  
            no[j]=no[j+1]  
            no[j+1]=temp
            temp=value[j]
            value[j]=value[j+1]
            value[j+1]=temp
ans=" ".join(value)
print(ans)            