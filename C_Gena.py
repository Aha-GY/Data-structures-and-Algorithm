n = int(input())
aastu = list(map(int,input().split()))
m = int(input())
aait = list(map(int,input().split()))
aastu.sort()
aait.sort()
i =0
j =0
count =0
while i < n and j< m:
    if abs(aait[j] - aastu[i]) < 2:
        count +=1
        i+=1
        j+=1
    elif aait[j] > aastu[i]:
        i +=1
    else:
        j +=1
print(count)