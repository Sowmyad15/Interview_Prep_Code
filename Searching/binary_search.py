def binary_search(a,key):
    start=0
    end=len(a)-1
    while start<=end:
        mid=start+(end-start)//2
        if key<a[mid]:
            end=mid-1
        elif key>a[mid]:
            start=mid+1
        else:
            return mid
    return -1




x=int(input("Enter no. of elements:"))
lst=[]
for i in range(x):
    m=int(input())
    lst.append(m)
key=int(input("Enter number to be searched:"))
flag=binary_search(lst,key)
if flag!=-1:
    print("Element found at index "+str(flag))
else:
     print("Element not found")
