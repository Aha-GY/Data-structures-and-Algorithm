t,k = map(int,input().split())
s = str(input())
left=0
count =0
max_str = 0
dic = { "a":0 ,"b":0}
for right in range(t):
    dic[s[right]] +=1
    min_count = min(dic["a"],dic["b"])
    while left<right and min_count > k:
        dic[s[left]] -=1
        min_count = min(dic["a"],dic["b"])
        left+=1
    max_str = max(max_str,right-left+1)
print(max_str)
