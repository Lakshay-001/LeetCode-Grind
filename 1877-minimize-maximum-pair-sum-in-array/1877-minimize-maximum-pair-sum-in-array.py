class Solution(object):
    def minPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        first=0
        last=len(nums)-1
        ans=0
        while first<last:
            par=nums[first]+nums[last]
            ans=max(ans,par)
            first+=1
            last-=1
        return ans


