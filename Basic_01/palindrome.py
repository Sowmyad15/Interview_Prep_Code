x=int(input("Enter a number:"))
sum=0
y=x
while y>0:
    tmp=y%10
    sum=(sum*10)+tmp
    y=y//10
if sum==x:
    print("Palindrome")
else:
    print("Not a Palindrome")