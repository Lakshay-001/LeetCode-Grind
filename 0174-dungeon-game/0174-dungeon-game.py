class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        m = len(dungeon)
        n = len(dungeon[0])
        dp = [[float('inf')] * (n+1) for _ in range(m+1)]
        dp[m][n-1] = 1
        dp[m-1][n] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                d = dp[i+1][j]
                r = dp[i][j+1]
                dp[i][j] = max(1, min(d, r) - dungeon[i][j])
        return dp[0][0]