# 371. Sum of Two Integers
# Medium

# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3

# Example 2:

# Input: a = 2, b = 3
# Output: 5
 
# Constraints:

# -1000 <= a, b <= 1000

n1=int(input("No1:"))
n2=int(input("No2:"))
ans=[i for i in range(-1000,1000)]
print(ans[1000+n1+n2])

