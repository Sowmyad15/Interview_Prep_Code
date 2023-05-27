def quick_sort(a,l,h):
    if l<h:
        pi=partition(a,l,h)
        quick_sort(a,l,pi-1)
        quick_sort(a,pi+1,h)


def partition(a,l,h):
    pivot=a[l]
    i=l+1
    j=h
    while True:
        while i<=j and a[j]>=pivot:
            j=j-1
        while i<=j and a[i]<=pivot:
            i=i+1
        if i<=j:
            a[i],a[j]=a[j],a[i]
        else:
            break
    a[l],a[j]=a[j],a[l]
    return j



#get a list of vaules to be sorted
x=int(input("Enter number of elements:"))
lst=[]
for i in range(0,x):
    n=int(input())
    lst.append(n)

print("Before Sort:")
print(lst)
print("After sort:")
quick_sort(lst,0,len(lst)-1)
print(lst)
