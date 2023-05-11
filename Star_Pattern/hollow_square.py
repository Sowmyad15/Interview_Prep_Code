x=int(input("Enter a number:"))
for i in range(x):
    for j in range(0,x):
        if i==0 or i==x-1 or j==0 or j==x-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("\n")
