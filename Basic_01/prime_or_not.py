x=int(input("Enter a number:"))
flag=0
if x<2:
    flag=1
else:
    for i in range(2,int(x/2)):
        if x%i==0:
            flag=1
if flag==1:
    print("NOT PRIME")
else:
    print("PRIME")