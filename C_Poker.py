import heapq

n = int(input())
for _ in range(n):
    t = int(input())
    nums = list(map(int,input().split()))
    maxheap =[]
    ans =0
    for i in range(t):
        if nums[i] != 0:
            heapq.heappush(maxheap,-nums[i])
        else:
            if maxheap:
                ans += heapq.heappop(maxheap)
    print(-ans)
