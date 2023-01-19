a=int(input("Enter the current year"))
b=int(input("Enter the ending year"))
print("The leap years are")
for i in range(a,b):
    if((i%400==0)or((i%100!=0)and(i%4==0))):
        if(i%2==0):
         print(i)