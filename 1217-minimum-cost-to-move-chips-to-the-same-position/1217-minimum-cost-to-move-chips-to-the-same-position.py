class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        odd=0
        eve=0
        for i in position:
            if i%2==0:
                eve+=1
            if i%2!=0:
                odd+=1
        return min(odd,eve)
                