l=int(input("Enter lower range:"))
u=int(input("Enter upper range:"))
for i in range(l,u):
    y=i
    sum=0
    while y>0:
        tmp=y%10
        sum+=(tmp*tmp*tmp)
        y=y//10
    if i==sum:
        print(i)        
