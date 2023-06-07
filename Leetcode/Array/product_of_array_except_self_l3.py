# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

print("Array:")
print(lst)

prod=[]

for i in range(0,x):
    p=1
    sub=lst[0:i]+lst[i+1:]
    for j in sub:
        p*=j
    
    prod.append(p)

print(prod)
