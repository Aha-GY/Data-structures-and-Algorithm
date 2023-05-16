arry = [3,4,9,7,5,1,0]
num=[]
for i in arry[:]:
    for j in arry[i+1:]:
        if j <i :
            i,j= j,i
            num.append(i)
print (arry)