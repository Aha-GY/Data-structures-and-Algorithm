t = int(input())
nums = list(map(int,input().split()))
nums.sort()
if t in nums:
  i = len(nums)//2-1
  for j in range(len(nums)):
    if  nums[i] == t:
      print(i)
      break
    
    elif t in nums[:i]:
      i = len(nums[:i])//2
    else:
      i = len(nums[i:])//2 + len(nums[:i])-1
  
else:
  print('target not found')
