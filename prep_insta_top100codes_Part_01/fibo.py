a=1
b=1
x=int(input("Fibonacci series upto:"))
print(a)
print(b)
for i in range(3,x):
    tmp=a+b
    print(tmp)
    a=b
    b=tmp


