x=int(input("Enter a Number:"))
y=pow(x,2)
m=pow(10, len(str(x)))
if y%m==x:
    print("Automorphic Number")
else:
    print("Not Automorphic Number")


