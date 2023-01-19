lis =[]                      #declared an empty list
x=int(input("Enter the number of words to check : "))
print("Enter the words")
for i in range(0,x):
    y=input()
    lis.append(y)            #append is function to add words to list
def longest(lis):            #defined a function to find lengthy word
    return max(lis,key=len)
print("Lengthy word is '" + longest(lis) + "'")

                             # this is a comment line
                             # remove all comment line while writing the code in your notebook