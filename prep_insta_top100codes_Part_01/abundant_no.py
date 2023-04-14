x=int(input("Enter a number:"))
tmp=[]
for i in range(1,x):
    if x%i==0:
        tmp.append(i)
print(tmp)
if sum(tmp)>x:
    print("Abundant number")
else:
    print("Not Abundant Number")