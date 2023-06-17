class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        row=[1,0,1]
        col=[1,0,1]
        """
        row=[1]*len(matrix)
        col=[1]*len(matrix[0])
        for i in range(len(row)):
            for j in range(len(col)):
                if matrix[i][j]==0:
                    row[i]=0
                    col[j]=0
        for i in range(len(row)):
            for j in range(len(col)):
                if row[i]==0 or col[j]==0:
                    matrix[i][j]=0