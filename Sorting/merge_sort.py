def merge_sort(lst):
        
    if len(lst)>1:
        #get mid index
        mid=len(lst)//2
        #seprate lst into R and L
        L=lst[:mid]
        R=lst[mid:]
        #Continous split
        merge_sort(L)
        merge_sort(R)
        
        #Declare variables
        i=j=k=0
        
        #Compare 2 arrays assign the minimum in lst
        while i<len(L) and j<len(R):
            if L[i]<R[j]:
                lst[k]=L[i]
                i=i+1
            else:
                lst[k]=R[j]
                j=j+1
            k=k+1
        
        #if R[] got over
        while i<len(L):
            lst[k]=L[i]
            i=i+1
            k=k+1
        
        #if L[] got over
        while j<len(R):
            lst[k]=R[j]
            j=j+1
            k=k+1


#get a list of vaules to be sorted
x=int(input("Enter number of elements:"))
lst=[]
for i in range(0,x):
    n=int(input())
    lst.append(n)

print("Before Sort:")
print(lst)
print("After sort:")
merge_sort(lst)
print(lst)
