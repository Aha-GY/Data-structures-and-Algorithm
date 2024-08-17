t= int(input())
nums =[]
for _ in range(t):
    num = list(map(int,input().split()))
    nums.append(num)
nums.sort()
if t <= 2:
    print("YES")
else:
    tv1 ,tv2 =nums[0][1],nums[1][1]
    for i in range(2,t):
        if tv1 < nums[i][0]:
            tv1 = nums[i][1]
        elif tv2 < nums[i][0]:
            tv2 = nums[i][1]
            
        else:
            print("NO")
            break
    else:
        print("YES")

t= int(input())
nums =[]
for _ in range(t):
    num = list(map(int,input().split()))
    nums.append(num)
nums.sort()
tv1 ,tv2 =-1,-1
for i in range(t):
    if tv1 < nums[i][0]:
        tv1 = nums[i][1]
    elif tv2 < nums[i][0]:
        tv2 = nums[i][1]
        
    else:
        print("NO")
        break
else:
    print("YES")