class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        s = sum(nums)
        if abs(target) > s or (s + target) % 2 != 0:
            return 0
        t = (s + target) // 2
        dp = [0] * (t + 1)
        dp[0] = 1
        for num in nums:
            for j in range(t, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[t]