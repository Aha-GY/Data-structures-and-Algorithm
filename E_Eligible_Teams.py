t = int(input())
for _ in range(t):   
    n , r = map(int,input().split())
    nums = list(map(int,input().split()))
    nums.sort()
    nums = nums[::-1]
    tems,size =0,1
    for i in range(n):
        if nums[i]*size >= r:
            size =1
            tems +=1
        else:
            size +=1
    print(tems)
