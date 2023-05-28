x=int(input("Enter number of elements:"))
a=[]
for i in range(x):
    a.append(int(input()))


for i in range(0,x):
    for j in range(0,x-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print(a)

i=0

print("1st half ascending 2nd half descending:")
while i<= (x//2):
    print(a[i])
    i=i+1

j=x-1

while j> x//2:
    print(a[j])
    j=j-1



