n=int(input("enter the limit"))
li=[]
for i in range (n):
    x=int(input("enter the element"))
    li.append(x)
linew=[i*i for i in li if i>0]
print("the squares are",linew)