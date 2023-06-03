x=input("Enter a String:")
for ch in x:
    if 'A'<=ch<='Z' or 'a'<=ch<='z':
        flag=1
    else:
        flag=0
        break
if flag==1:
    print("Full of alpha")
else:
    print("Not full of alpha")