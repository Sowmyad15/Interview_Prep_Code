x=int(input("Enter a number:"))
ans=[]
while(x>0):
    ans.append(str(x%2))
    x=x//2

ans=ans[::-1]
b="".join(i for i in ans)
print(b)

#No.of ones
count=ans.count('1')
print(count)