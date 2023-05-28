x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

m=lst[0]
for i in lst:
    if i>m:
        m=i

print("Maximum Element:"+str(m))