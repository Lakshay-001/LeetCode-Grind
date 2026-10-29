class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = 0
        for i in range(n // 2):
            ans += (n-1)-2*i
        return ans