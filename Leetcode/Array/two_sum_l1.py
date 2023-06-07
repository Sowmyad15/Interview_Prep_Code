# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

x=int(input("Enter number of elements:"))
lst=[]
print("Enter array elements:")
for i in range(x):
    lst.append(int(input()))

target=int(input("Enter target:"))

print(lst)

index=[]
for i in range(0,x):
    for j in range(i+1,x):
        if lst[i]+lst[j]==target:
             index.append(i)
             index.append(j)

print(index)