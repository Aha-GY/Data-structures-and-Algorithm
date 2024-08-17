t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    odd =0
    even =0
    for num in nums:
        if num%2:
            odd +=1
        else:
            even +=1
    if min(odd,even) >= n:
        print("Yes")
    else:
        print("No")