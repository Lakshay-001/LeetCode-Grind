class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxx=float("-inf")
        for i in accounts:
            a=sum(i)
            if a>=maxx:
                maxx=a
        return maxx


        