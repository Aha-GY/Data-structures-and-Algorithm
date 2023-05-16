arry=[6,2,7,5,3,0,8,4]
for i in range(len(arry)-1,0,-1):
    for j in range (i):
        if arry[j]>arry[j+1]:
            temp=arry[j].
            arry[j]=arry[j+1]
            arry[j+1]=temp
print(arry)