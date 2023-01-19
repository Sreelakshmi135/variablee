num=int(input("enter a number"))
k=0
i=2
while(i<num):
    if(num%i==0):
     k=1
     i+=1
if(k==0):
        print("prime")
else:
        print("not prime")