x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

print("Array:")
print(lst)

flag=False

for i in range(0,x):
    if lst[i] in lst[i+1:x]:
        flag=True
        break
    else:
        flag=False

print(flag)