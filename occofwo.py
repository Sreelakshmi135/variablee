n=input("enter the string").split(' ')
li1=list(n)
set=set(li1)
linew=list(set)
for i in linew:
    count=0
    for j in li1:
        if i==j:
            count=count+1
            print("occurance of",i,count)
