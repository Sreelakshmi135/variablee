list=[]
x=int(input("enter the number of string"))
m=0
for i in range (x):
    a=input("enter the name")
    list.append(a)
    for i in list:
        c=i.count("a")
        m=m+c
        print("count of a is",m)
