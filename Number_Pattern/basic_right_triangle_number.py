x=int(input("Enter number of rows:"))
k=1
for i in range(x):
    for j in range(0,i+1):
        print(k,end=" ")
        k=k+1
    print()