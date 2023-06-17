class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        a=height
        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            area=(j-i)*min(a[i],a[j])
            max_area=max(area,max_area)
            if a[i]<a[j]:
                i=i+1
            else:
                j=j-1
        return max_area