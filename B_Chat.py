import heapq

n,k,q = map(int,input().split())
nums = list(map(int,input().split()))
ans =[]

for i in range(q):
    online,idx = map(int,input().split())

    if online == 1:
        if len(ans) <k:
            heapq.heappush(ans,(nums[idx-1],idx))
        else:
            heapq.heappushpop(ans,(nums[idx-1],idx))
    elif online == 2:
        temp ="NO"
        for val, i in ans:
            if i == idx:
                temp ="YES"
                break
        print(temp)