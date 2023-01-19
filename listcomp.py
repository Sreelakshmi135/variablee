n=int(input("enter the limit"))
li=[]
for i in range(n):
    a=int(input("enter the element"))
    li.append(a)
    print("the list entered is:",li)
    linew=[i for i in li if i>0]
    print("the new list is",linew)