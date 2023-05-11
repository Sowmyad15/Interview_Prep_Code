r=int(input("No.of rows:"))
c=int(input("No.of cols:"))
for i in range(r):
    for k in range(i):
        print(" ",end=" ")
    for j in range(c):
        print("*",end=" ")
    print("\n")