x=int(input("Enter a number:"))
y=x
sum=0
while(y>0):
    tmp=y%10
    sum+=tmp
    y=y//10

if x%sum==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")