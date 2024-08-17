for _ in range(int(input())):
    n = int(input())
    print(1 + (n == 1) if n <= 3 else (n + 2) // 3)