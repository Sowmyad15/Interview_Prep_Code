# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

print("Array:")
print(lst)

for i in range(0,x):
    sub=[]
    for j in range(i+1,x):
        sub.append(lst[i])
        sub.append(lst[j])
    print(sub)