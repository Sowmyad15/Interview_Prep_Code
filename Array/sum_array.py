x=int(input("Enter number of elements:"))
a=[]
for i in range(x):
    a.append(int(input()))

sum=0

for i in a:
    sum=sum+i

print("Sum of elements in array:"+str(sum))