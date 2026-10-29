class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        count=0
        costs.sort()
        for i in costs:
            if i<=coins:
                count+=1
                coins-=i
        return count