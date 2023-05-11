x=int(input("Enter number of rows:"))
k=3
for i in range(x):
    for j in range(i+1):
        print(k,end=" ")
    k=k+1
    print()
for i in range(x-1):
    k=k-1
    for j in range(x-i-1):
        print(k-1,end=" ")
    print()