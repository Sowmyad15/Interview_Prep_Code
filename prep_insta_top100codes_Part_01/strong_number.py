x=int(input("Enter a number:"))
y=x
sum=0
while(y>0):
    tmp=y%10
    fact=1
    while tmp>0:
        fact*=tmp
        tmp=tmp-1
    sum+=fact
    y=y//10
if sum==x:
    print("Strong Number")
else:
    print("Not a Strong Number")