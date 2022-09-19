arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
num=[i for i,j in enumerate(arr) if j>0] #Список с положительными
max_num=[]
##sum_i=0
sum_i1=0
j=0
##def save(sum_i1):
##    append.max_num(sum_i1)
##    return max(max_num)
def start(j):
    sum_i=arr[num[j]]
    for i in range(j,len(num)-1):
        sum_i1=sum_i
        print ('j',j,'\nsum_i1',sum_i1,'\ni',i,'\ni:i+1',arr[num[i]:num[i+1]+1])
        sum_i=sum(arr[num[i]+1:num[i+1]+1],sum_i)
        print ('sum_i',sum_i,'\n sum_i-arr[num[i+1]]',sum_i-arr[num[i+1]])
        if sum_i-arr[num[i+1]]>0:
            if sum_i<sum_i1:
                max_num.append(sum_i1) #Запоминает максимальную сумму подпоследовательности
                if j==len(num)-1:
                    print ('max_num',max_num)
                    break
                print (j)
                j+=1
                return j #Запускает цикл в цикле с началом в j+1
        else:
            sum_i=arr[num[i]]
            continue
start(j)
