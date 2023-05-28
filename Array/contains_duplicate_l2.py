# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

x=int(input("Enter number of elements:"))
lst=[]
for i in range(x):
    lst.append(int(input()))

print("Array:")
print(lst)

flag=False

for i in range(0,x):
    if lst[i] in lst[i+1:x]:
        flag=True
        break
    else:
        flag=False

print(flag)