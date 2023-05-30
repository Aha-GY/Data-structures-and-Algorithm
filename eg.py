n=6
m= 7
a1= [1,6,9,13,18,18]
b1= [2,3,8,13,15,21,25]


merg=[]
i=1
while i< n+m:
    if a1[i]<= b1[i]:
        merg.append(a1[i])
    merg.append(b1[i])
print(merg)

        