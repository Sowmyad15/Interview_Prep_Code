x=input("Enter a String:")
a=[]
for i in x:
    a.append(i)
a.sort()
str1=""
for i in a:
    str1+=i
print("Ordered String:"+str1)