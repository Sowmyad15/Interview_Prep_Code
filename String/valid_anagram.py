str1=input("Enter str1:")
str1.lower()
str2=input("Enter str2:")
str2.lower()
flag=0
for i in str1:
    if i in str2:
        flag=1
    else:
        break

if flag==1:
    print("Anagram")
else:
    print("Not a anagram")