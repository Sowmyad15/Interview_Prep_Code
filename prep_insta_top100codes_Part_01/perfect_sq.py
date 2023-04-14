x=int(input("Enter a number:"))
sum=0
for i in range(1,x//2+1):
    if x%i==0:
        sum+=i
if sum==x:
    print("Perfect Square")
else:
    print("Not a perfect square")