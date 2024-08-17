t = int(input())
nums = list(map(int, input().split()))

frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1
    
max_frequency = max(frequency.values())
result = t - max_frequency

print(result)
