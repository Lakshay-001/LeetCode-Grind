class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n=len(isConnected)
        visited=[]
        count=0
        def dfs(city):
            visited.append(city)
            for i in range(n):
                if isConnected[city][i]==1 and i not in visited:
                    dfs(i)
        for j in range(n):
            if j not in visited:
                count += 1
                dfs(j)
        return count

