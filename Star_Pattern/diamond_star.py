x=int(input("Enter a number:"))
for i in range(x):
    for spc in range(x-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print("\n")
for i in range(x-1):
    for spc in range(i+1):
        print(" ",end=" ")
    for j in range(x-(2*i-1)):
        print("*",end=" ")
    print("\n")