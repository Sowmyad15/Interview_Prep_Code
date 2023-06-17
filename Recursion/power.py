def power_of_no(a,b):
    if b!=0:
        return a*power_of_no(a,b-1)
    else:
        return 1
    
x=int(input("Enter a:"))
y=int(input("Enter b:"))
print(power_of_no(x,y))