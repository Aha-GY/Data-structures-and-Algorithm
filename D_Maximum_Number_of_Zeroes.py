from collections import Counter
from fractions import Fraction

n = int(input())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

ans = []
for i in range(n):
    if nums2[i] == 0:
        ans.append(0)
    elif nums1[i] == 0:
        ans.append(float("inf"))
    else:
        ans.append(Fraction(-nums2[i], nums1[i]))

count = Counter(ans)
max_count = max(count.values())

for key, val in count.items():
    if max_count == val:
        if key == float("inf"):
            print(0)
        else:
            print(val)
        break
