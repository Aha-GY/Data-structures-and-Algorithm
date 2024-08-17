t = int(input())
for _ in range(t):
    n,total = map(int,input().split())
    demand = list(map(int,input().split()))
    time = list(map(int,input().split()))

    if total < sum(time):
        print(-1)
    else:
        temp = 0
        for i in range(n):
            temp +=(time[i]*demand[i])
        min_dem = ((temp+1)//total)
        j =1
        while True:
            temp =0
            check = min_dem -j
            for i in range(n):
                temp += ((demand[i]+1)//check ) * time[i]
            if temp > total:
                print(check+1)
                break
            j +=1