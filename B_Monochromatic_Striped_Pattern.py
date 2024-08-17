t = int(input())
for _ in range(t):
    n , k = map(int, input().split())
    box = str(input())
    left =0
    w_count =0
    
    for i in range(k):
        if box[i] =="W":
            w_count +=1
    min_opration = w_count
    for right in range(k,n):
        if box[right] == "W":
            w_count +=1
        if box[left] == "W":
            w_count -=1
        left +=1
        min_opration = min(min_opration , w_count)
    print(min_opration)
