a=[1]
b=[]
def prov(a,b):
    h=True
    for i in a:
        if h==False:
            break
        else:
            for y in b:
                if i**2==y:
                    h=True
                    print (i,y)
                    b.remove(y)
                    break
                else:
                    h=False
    return h
def comp(a, b):
    print (a,b)
    if a==None or b==None or a==[] or b==[0]:
        p=False
    else:
        p=prov(a,b)
    return p
