x=int(input("Enter Year:"))
if(x%4==0 or x%400==0)and x%100!=0:
    print("Leap Year")
else:
    print("Not a Leap Year")