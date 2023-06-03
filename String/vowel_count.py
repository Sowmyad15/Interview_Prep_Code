x=input("Enter a String:")
count=0
for ch in x:
    if ch=='A'or ch=='E'or ch=='I'or ch=='O'or ch=='U'or ch=='a'or ch=='e'or ch=='i'or ch=='o'or ch=='u':
        count+=1
print("Vowels:"+str(count))