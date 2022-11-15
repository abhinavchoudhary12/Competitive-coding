a=input()
b=input()

def st(a,b):
    c=[]
    al=len(a)
    bl=len(b)
    if al>bl:
        tl=al
    else:
        tl=bl


    for i in range(tl):
        if i<al:
            c.append(a[i])
        else:
            pass
        if i<bl:
            c.append(b[i])
        else:
            pass
    ans=''.join(c)

    anser=ans[:]
    anser1=anser.lower()
    return anser1

print(st(a,b))