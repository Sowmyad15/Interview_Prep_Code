x=int(input("Enter number of elements:"))
lst=[]
print("Enter array elements:")
for i in range(x):
    lst.append(int(input()))

target=int(input("Enter target:"))

print(lst)

index=[]
for i in range(0,x):
    for j in range(i+1,x):
        if lst[i]+lst[j]==target:
             index.append(i)
             index.append(j)

print(index)