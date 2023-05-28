x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

mini=lst[0]
maxi=lst[0]

for i in lst:
    if i<mini:
        mini=i
    
    if i>maxi:
        maxi=i

print("Maximum Element:"+str(maxi))
print("Minimum Element:"+str(mini))
