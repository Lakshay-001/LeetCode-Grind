class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        MOD = 10**9 + 7

        dp = [[-1] * n for _ in range(m)]

        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            ans = 1

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if (0 <= x < m and 0 <= y < n
                    and grid[x][y] > grid[i][j]):

                    ans += dfs(x, y)

            dp[i][j] = ans % MOD
            return dp[i][j]

        total = 0

        for i in range(m):
            for j in range(n):
                total += dfs(i, j)

        return total % MOD