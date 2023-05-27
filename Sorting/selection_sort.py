def selection_sort(x,lst):
    for i in range(x):
        min_index=i
        for j in range(i+1,x):
            if lst[i]>lst[j]:
                min_index=j
        temp=lst[i]
        lst[i]=lst[min_index]
        lst[min_index]=temp




x=int(input("Enter number of elements:"))
lst=[]
for i in range(0,x):
    n=int(input())
    lst.append(n)

print("Before Sort:")
print(lst)
print("After sort:")
selection_sort(x,lst)
print(lst)