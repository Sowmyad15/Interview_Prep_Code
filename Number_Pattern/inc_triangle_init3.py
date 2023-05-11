x=int(input("Enter number of rows:"))
k = 0
for i in range(x, 0, -1):
    k = k + i
for i in range(x):
    for j in range(x-i):
        print(k,end=" ")
    k=k-1
    print()