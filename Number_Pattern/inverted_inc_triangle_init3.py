x=int(input("Enter number of rows:"))
k=3
for i in range(x):
    for j in range(i+1):
        print(k,end=" ")
    k=k+1
    print()