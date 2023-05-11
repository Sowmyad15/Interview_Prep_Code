x=int(input("Enter a number:"))
for i in range(x):
    for j in range(x-1):
        if i==0 or i==x-1 or j==0 or j==x-2:
            print(x-1,end=" ")
        else:
            print(i,end=" ")
    print()