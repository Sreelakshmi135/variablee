l1=[34,27,93,-38]
l2=[34,-79,37,-89]
x=len(l1)
y=len(l2)
s1=sum(l1)
s2=sum(l2)
if(x==y):
    print("list are of same length")
else:
      print("different")
if(s1==s2):
    print("sum of two lists are same")
else:
     print("sum is different")
     print("common elements")
for i in l1:
    for j in l2:
      if(i==j):
         print(i)