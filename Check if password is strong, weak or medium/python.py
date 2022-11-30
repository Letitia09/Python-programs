a=input()
lcase,ucase,dig,char=0,0,0,0
e=['#','*','@','$','%','!','?']
Lower_case=[chr(x) for x in range(97,123)]
Upper_case=[chr(x) for x in range(65,91)]

for i in range(len(a)):
    if a[i] in Lower_case:
        lcase+=1
    if a[i] in Upper_case:
        ucase+=1 
    if a[i].isdigit():
        dig+=1
    if a[i] in e:
        char+=1 
if lcase>=1 and ucase>=1 and dig>=1 and char>=1:
    print("strong")
else:
    w=[lcase,ucase,dig,char]
    count=0
    for i in range(len(w)):
        if w[i]>=1:
            count+=1
    if count<2:
        print("medium")
    else:
        print("weak")
