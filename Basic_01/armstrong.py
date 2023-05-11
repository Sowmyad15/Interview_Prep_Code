x=int(input("Enter a number:"))
sum=0
y=x
while y>0:
    tmp=y%10
    sum+=tmp*tmp*tmp
    y=y//10
if sum==x:
    print("Armstrong")
else:
    print("Not a Armstrong")