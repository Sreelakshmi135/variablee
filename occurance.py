str=input("enter the string")
word=input("enter the word")
count=0
str1=str.split(' ')
for i in str1:
    if(i==word):
        count=count+1
    print(count)