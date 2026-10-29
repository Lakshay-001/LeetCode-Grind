class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ans = 0
        # for i in range(n // 2):
        #     ans += n-(2*i+1)
        # return ans
        return n * n // 4