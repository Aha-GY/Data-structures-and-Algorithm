s= "i3 and2 you1 have4 time6 good5"
word = list(s)
good_word = []
for i in word :
    n=1
    if i == n :
        good_word.append(i)
        n += 1
print(good_word)
return ' '.join([w[:-1] for w in sorted(s.split(),key=lambda x:x[-1])])