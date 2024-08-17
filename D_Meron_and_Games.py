import sys, threading
from collections  import Counter
input = lambda: sys.stdin.readline().strip()

def main():
    t = int(input())
    nums = list(map(int,input().split()))
    memo ={}
    count = Counter(nums)
    m  = max(nums)
    def dp(idx):
        if idx > m: return 0
        if idx not in memo:
        
            pick = count[idx]*idx + dp(idx +2)
            notPick = dp(idx+1)
            _max = max(pick , notPick)
            memo[idx] = _max
        
        return memo[idx]
    print(dp(0))

    
if __name__ == '__main__':
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()


