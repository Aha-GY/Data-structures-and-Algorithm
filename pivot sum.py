nums = [1,7,3,6,5]
pivot_sum = sum(nums)//2
pre_sum = [0]

for num in nums:
    tmp = pre_sum[-1] + num
    pre_sum.append(tmp)
    if pivot_sum == pre_sum:
        print(num) 
