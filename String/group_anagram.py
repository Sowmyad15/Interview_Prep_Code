n=int(input("Enter length of the list:"))
a=[]
for i in range(0,n):
    a.append(input())
d={}
for i in a:
    word="".join(sorted(i))
    if word not in d:
        d[word]=[i]
    else:
        d[word]+=[i]

f=[]
for i in d:
    f.append(d[i])

print(f)

