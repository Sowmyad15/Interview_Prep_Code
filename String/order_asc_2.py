x=input("Enter a String:")
ch=list(x)
for i in range(0,len(ch)):
    for j in range(0,len(ch)-i-1):
        if ch[j]>ch[j+1]:
            ch[j],ch[j+1]=ch[j+1],ch[i]
print("Ordered String:"+"".join(ch))