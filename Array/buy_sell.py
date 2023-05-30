# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

x=int(input("Enter number of elements:"))
a=[]
for i in range(x):
    a.append(int(input()))

max_profit=0
l=0     #left->buy
r=1     #right->sell
while r<x-1:
    curr_profit=a[r]-a[l]
    if a[l]<a[r]:
        max_profit=max(curr_profit,max_profit)
    else:
        l=l+1
    r=r+1

print("Max profit:")
print(max_profit)

