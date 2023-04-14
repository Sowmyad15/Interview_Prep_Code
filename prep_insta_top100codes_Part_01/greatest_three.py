a=int(input())
b=int(input())
c=int(input())
if (a>b)and(a>c):
    print(str(a)+" is greater")
elif((b>c)and(b>a)):
    print(str(b)+" is greater")
else:
    print(str(c)+" is greater")