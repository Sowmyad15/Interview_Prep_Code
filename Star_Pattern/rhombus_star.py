x=int(input("Enter a number:"))
for i in range(x):
    for spc in range(i):
        print(" ",end=" ")
    for j in range(x):
        print("*",end=" ")
    print("\n")