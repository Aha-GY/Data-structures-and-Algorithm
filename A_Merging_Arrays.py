n, m =  map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
merg_nums =[]
i=0
j=0
while i<n and j<m :
   if arr2[j]>=arr1[i]:
      merg_nums.append(arr1[i])
      i+=1
   else:
      merg_nums.append(arr2[j])
      j+=1
if j<m:
   for j in arr2[j:]:
      merg_nums.append(j)
      j+=1
elif i<n:
   for i in arr1[i:]:
      merg_nums.append(i)
      i+=1
print(*merg_nums)


