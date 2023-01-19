n=int(input("enter the value of elements"))
print("enter the elements")
list=[]
for i in range(0,n):
    k=int(input())
    if (k%2!=0):
        list.append(k)
print(list)
