a=[] #declaring a an empty list
#a=[2,23.59,"Hello",'Hi',2+3j] - here the list is intialised
n=int(input("enter a value for knowing the length of list : ")) # n indicates the length of list taken from the user
for i in range(0,n):
    x=int(input("enter the value :"))  #here for each iteration the user gives an input to store the data in list
    a.append(x) # here you are adding the value of x into the list 'a' from the end
print(a) # it will display all the values which are stored in the list 'a'
