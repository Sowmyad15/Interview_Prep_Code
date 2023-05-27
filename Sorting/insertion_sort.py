def insert_sort(x,lst):
    for i in range(1,x):
        j=i-1
        key=lst[i]
        while j>=0 and key<lst[j]:
            lst[j+1]=lst[j]
            j=j-1
        lst[j+1]=key



x=int(input("Enter number of elements:"))
lst=[]
for i in range(0,x):
    n=int(input())
    lst.append(n)

print("Before Sort:")
print(lst)
print("After sort:")
insert_sort(x,lst)
print(lst)