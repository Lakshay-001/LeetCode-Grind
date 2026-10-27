class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False

        return True
