class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        if len(original)!=m*n:
            return []
        arr=[[0]*n for _ in range(m)]
        for i in range(0,m):
            for j in range(0,n):
                arr[i][j]=original[i*n+j]
        return arr
