x=int(input("Enter a number:"))
for i in range(x):
    for spc in range(x-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(x):
    for spc in range(i+1):
        print(" ",end=" ")
    for j in range(x-i-1):
        print("*",end=" ")
    print("\n")