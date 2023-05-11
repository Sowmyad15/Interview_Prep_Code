x=int(input("Enter a number:"))
for i in range(x):
    for spc in range(i):
        print(" ",end=" ")
    for j in range(2*i,x*2-1):
        print("*",end=" ")
    print("\n")