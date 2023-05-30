x=int(input("Enter number of elements:"))
a=[]
for i in range(x):
    a.append(int(input()))

ans=set()
a.sort()
for i in range(0,x-2):
    j=i+1
    k=x-1
    num1=a[i]
    while j<k:
        num2=a[j]
        num3=a[k]

        trip_sum=num1+num2+num3
        if trip_sum==0:
            ans.add((num1,num2,num3))
            j=j+1
            k=k-1
        elif trip_sum<0:
            j=j+1
           
        else:
            k=k-1
          

print("Unique Triplets:")
print(ans)
