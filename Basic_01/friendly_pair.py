x=int(input("Enter a number 1:"))
y=int(input("Enter a number 2:"))

def divisor(x):
    a=[]
    for i in range(1,x):
        if x%i==0:
            a.append(i)
    q1=sum(a)//x
    return q1

if divisor(x)==divisor(y):
    print("Friendly Pair")
else:
    print("Not a Friendly Pair")
