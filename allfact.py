number=int(input("enter a number"))
print("the factores are".format(number))
for i in range(1,number+1):
    if number % i==0:
      print(i)

