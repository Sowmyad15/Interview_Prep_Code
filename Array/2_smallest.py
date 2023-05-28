x=int(input("Enter number of elements:"))
a=[]
for i in range(x):
    a.append(int(input()))

for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print("Second largest in array:"+str(a[x-2]))


