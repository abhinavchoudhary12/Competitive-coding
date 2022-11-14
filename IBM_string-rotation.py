
def rotate(n,lo):
    a=n.split(' ')
    li=[]
    count=int(lo[1])
    print(lo[0])
    b=lo[0]
    if b in ['r','R']:
        for i in a:
            f=i[:len(i)-count]
            l=i[len(i)-count:]
            a=l+f
            
            li.append(a)
        li=' '.join(li)
        return li
    if b in['l','L']:
        for i in a:
            print("hh")
            f=i[:count]
            l=i[count:]
            a=l+f
            
            li.append(a)
        li=' '.join(li)
        return li
        
n=input()  
b=input()
print(rotate(n,b))