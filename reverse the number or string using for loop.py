number=input()
x=int(number)
print("the number before reversing is : ",x)
print("the number after reversing is :  ")
for i in range(len(number)):
        rev=x%10
        x//=10
        print(str(rev),end="")
