t = int(input())
for _ in range(t):
    n = int(input())
    nums1 = list(map(int,input().split()))
    nums2 = list(map(int,input().split()))
    nums2.sort()
    nums1.sort()
    ans =[]
    i,j =0,0
    while i< n and j<n:
        if nums1[i] < nums2[j]:
            ans.append(nums1[i])
            i+=1
        elif nums1[i] == nums2[j]:
            ans.append(nums1[i])
            ans.append(nums2[j])
            i+=1
            j+=1
        else:
            ans.append(nums2[j])
            j+=1
    equal_num =1
    max_equal_num=0
    for i in range(1,len(ans)):
        if ans[i] == ans[i-1]:
            equal_num+=1
        else:
            equal_num =1
        max_equal_num = max(max_equal_num,equal_num)
    print(max_equal_num)