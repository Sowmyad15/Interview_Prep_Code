x=int(input("Enter a number:"))
print("Factorial:")
fact=1
while x>0:
    fact*=x
    x=x-1
print(fact)