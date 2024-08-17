t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    count =0
    
    coll ={}
    for i in range(n):
        coll[i] = nums[i]
    temp = [coll.values()]
    new_temp = sorted(temp.sort())
    print(temp)
    i =0
    j=n-1
    # while i<j:

    #     if nums[j] - nums[i] == j-i:
    #         count+=1
    #         i+1
    #     else:

    print(count)
