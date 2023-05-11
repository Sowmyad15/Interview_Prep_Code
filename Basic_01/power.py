x=int(input("Enter number:"))
y=int(input("To the power:"))
sum=1
for i in range(1,y+1):
    sum*=x
print(sum)