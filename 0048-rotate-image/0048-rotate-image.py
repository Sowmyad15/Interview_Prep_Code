class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        u=0
        l=len(matrix)-1
        while u<l:
            matrix[u],matrix[l]=matrix[l],matrix[u]
            u=u+1
            l=l-1
        
        for i in range(len(matrix)):
            for j in range(i):
                 matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]