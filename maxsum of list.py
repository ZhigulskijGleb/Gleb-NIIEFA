arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
pos=arr.copy()
num=[]
max_sum=[0]
##arr.append(0)
##arr.append(0)
##n=[]
##for i in range(0,len(arr)-2):
##    sum=arr[i]+arr[i+1]
##    if sum>arr[i+2]:
##        continue
##    else:
##        n.append(sum)
##        sum=0
def max_sequence(arr):
    print (arr)
    if arr==[]:
        return 0
    num=[]
    max_sum=[]
    for i in range(len(arr)):
        if arr[i]>0:
            num.append(i)
    if len(num)==0:
        return 0
    sum=arr[num[0]]
    arr.append(0)
    count=arr[num[0]]
    for i in range(1,len(num)-1):
        print ('на входе',sum)
        for n in arr[num[i]:num[i+1]+1]:
            sum+=n
        print ('сумма после цикла',sum)
        print ('count',count)
        print ('arr',arr[num[i+1]])
        if sum>count or (sum>arr[num[i+1]] and sum>arr[i]):
            count=sum
            sum-=arr[num[i+1]]
        else:
            max_sum.append(sum+arr[num[i]])
            sum=0
            count=arr[num[i+1]]
            
        print ('на выходе',arr[num[i]:num[i+1]+1], sum)
        print(max_sum)
    if max_sum==[]:
        max_sum.append(sum+arr[num[-1]])
    return (max(max_sum))  


