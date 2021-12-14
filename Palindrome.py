a=1001

rev=0

original =a

while a!=0:
    
    rev=rev*10+a%10
    
    a//=10
    
if rev==original:
    
    print(original,"is a palindrome")

else:
    
    print(original,"is not a palindrome")

