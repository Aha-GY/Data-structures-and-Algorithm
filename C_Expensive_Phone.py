t = int(input())
for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))
    m_stack =[]
    count =0
    for i in range(n):
        while m_stack and m_stack[-1] > nums[i]:
            m_stack.pop()
            count += 1
        m_stack.append(nums[i])
    print(count)