def bubble(x,lst):
    for i in range(x):
        for j in range(0,x-i-1):
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp


x=int(input("Enter number of elements:"))
lst=[]
for i in range(0,x):
    n=int(input())
    lst.append(n)

print("Before Sort:")
print(lst)
print("After sort:")
bubble(x,lst)
print(lst)





