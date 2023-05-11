x=int(input("Enter a number:"))
for i in range(x):
    for spc in range(i):
        print(" ",end=" ")
    for j in range(2*i,x*2-1):
        if i==0 or i==x-1 or j==2*i or j==2*x-2:
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print("\n")