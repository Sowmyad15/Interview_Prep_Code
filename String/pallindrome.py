x=input("Enter a word:")
flag=0
j=-1
for i in range(len(x)//2):
    if x[i]!=x[j]:
        flag=1
        break
    j=j-1

if flag==0:
    print("Pallindrome")
else:
    print("Not a Pallindrome")






