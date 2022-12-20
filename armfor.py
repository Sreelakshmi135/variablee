a=int(input("enter a number"))
x=a
y=0
for i in range(x,0,-1):
    s=x%10
    y=y+(s*s*s)
    x=x//10
if(y==a):
    print("armstrong number",a)
else:
    print("is not a amstrong",a)
