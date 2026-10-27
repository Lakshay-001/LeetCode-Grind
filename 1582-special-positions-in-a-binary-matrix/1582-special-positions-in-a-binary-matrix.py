class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        n=len(mat)
        m=len(mat[0])
        c=0
        for i in range(m):
            ro=0
            co=0
            for j in range(n):
                # print(mat[j][i])
                if mat[j][i]==1:
                    ro+=1
            if ro == 1:
                for j in range(n):
                    if mat[j][i] == 1 and sum(mat[j]) == 1:
                        c += 1

        return c