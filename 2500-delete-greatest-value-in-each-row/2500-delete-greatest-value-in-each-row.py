class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n=len(grid)
        m=len(grid[0])
        ans=0
        # if (n-1)==m and m==0:
        #     return grid[0][0]
        while m>0:
            arr=[]
            for i in range(n):
               a = max(grid[i])
               arr.append(a)
               print(a)
               grid[i].remove(a)
            ans+=max(arr)
            m-=1
        return ans
        



