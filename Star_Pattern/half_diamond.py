x=int(input("Enter an odd number:"))
for i in range(x):
    for j in range(i+1):
        print("*",end=" ")
    print("\n")
for i in range(x):
    for j in range(x-i-1):
        print("*",end=" ")
    print("\n")