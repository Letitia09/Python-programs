l=list(map(int,input().split()))
l.sort()
for i in range(1,len(l)):
    if l[i-1]+1 == l[i]:
        continue
    else:
        print(l[i-1]+1)
