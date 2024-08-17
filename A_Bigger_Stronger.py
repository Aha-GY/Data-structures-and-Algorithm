from collections  import Counter 
t = int(input())
for _ in range(t):
    n = int(input())
    nums= list(map(int,input().split()))
    count = Counter(nums)
    for val in count:
        if count[val] >= 2:   
            print("NO")
            break
    else:
        print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    nums= list(map(int,input().split()))
    for i in range(len(nums)):
        if nums[i] in nums[i+1:]:
            print("NO")
            break
    else:
        print("YES")

t = int(input())
for _ in range(t):
    n = int(input())
    nums= list(map(int,input().split()))

    print("YES") if len(nums) == len(set(nums)) else print("NO")
        
    