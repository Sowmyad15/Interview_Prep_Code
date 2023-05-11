x=int(input("Enter a number:"))
sum=0
while x>0:
    tmp=x%10
    sum=(sum*10)+tmp
    x=x//10
print(sum)

