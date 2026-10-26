class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """

        su=0
        n=len(mat)
        if(n==0):
            return []
        if(n==1):
            return mat[0][0]
        right=len(mat[1])-1
        for i in range(n):
            su+=(mat[i][i])
            if (n-i-1)!=i:
                su+=mat[i][n-i-1]
        return su