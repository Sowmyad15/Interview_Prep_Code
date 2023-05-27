x=int(input("Enter no. of elements:"))
lst=[]
for i in range(x):
    m=int(input())
    lst.append(m)

flag=False

key=int(input("Enter number to be searched:"))
for i in range(0,len(lst)):
    
    if lst[i]==key:
        index=i
        flag=True
        break
    else:
        flag=False
    
if flag==True:
    print("Element found at index "+str(index))
else:
    print("Element not found")
    