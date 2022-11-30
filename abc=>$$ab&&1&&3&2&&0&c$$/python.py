s=input()
n=int(input())
countodd=1
if len(s)%2!=0:
    s=s+'$'
    countodd+=1
def func(s,countodd):
    if len(s)%2!=0:
        if countodd%2!=0:
            s=s+'$'
        else:
            s='$'+s
        countodd+=1
    return s,countodd
for i in range(n):
    if len(s)%2==0:
        e=len(s)//2
        s=s[:e]+'&'+str(i)+'&'+s[e:]
        if i!=n-1:
            s,countodd=func(s,countodd)
        print(i,s)
        
