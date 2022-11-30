a=input()
l=[]
for i in range(len(a)):
    if a[i]=='a' or a[i]=='e' or a[i]=='i' or a[i]=='o' or a[i]=='u':
        continue
    else:
        if a[i] not in l:
            l.append(a[i])
for i in range(len(l)):
    print(l[i]," ",a.count(l[i]))
