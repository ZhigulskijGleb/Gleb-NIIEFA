arr=[1,2,3,3,3,4,5,6,6,6,7,7,8]
d={}
count=[]
c=list(set(arr))
for i in c:
    count.append(arr.count(i))
for i in range(len(c)-1):
    d[c[i]]=count[i]
print (d)
    

