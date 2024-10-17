class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        d = {}
        length = 0
        
        for r in range(len(s)):
            c = s[r]
            if c in d and d[c] >= l:  # If the character is already in the current window
                l = d[c] + 1  # Move the left pointer to avoid repeating the character
            
            d[c] = r  # Update the position of the character
            length = max(length, r - l + 1)  # Calculate the maximum length
        
        return length
