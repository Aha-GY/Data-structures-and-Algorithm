t = int(input())
for i in range(t):
    lett = str(input())
    reff = "codeforces"
    cont = 0
    for i in range(len(lett)):
        if lett[i] != reff[i]:
            cont +=1
    print(cont)