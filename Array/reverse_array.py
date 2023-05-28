x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

print("Array:")
print(lst)

print("Reverse Array:")

start=0
end=len(lst)-1

while start<end:
    lst[start],lst[end]=lst[end],lst[start]
    start=start+1
    end=end-1

print(lst)

