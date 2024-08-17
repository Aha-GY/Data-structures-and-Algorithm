
t = int(input())
colo = str(input())
no_que =0
for i in  range(t):
    if i>0 and colo[i] != "?":
        if colo[i] == colo[i-1]:
            print("No")
            break
    elif  colo[i] == "?":
        no_que +=1
else:
    if no_que >1 :
        print("Yes")
    else:
        if colo[0] != colo[-1] and len(colo) ==3:
            print("No")
        else:
            print("Yes")
        
