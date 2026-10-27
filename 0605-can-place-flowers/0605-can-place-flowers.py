class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        l=len(flowerbed)
        t=0
        i=0
        while i<l:
            if flowerbed[i]==1:
                i+=2
            elif flowerbed[i]==0:
                left=(i==0 or flowerbed[i-1]==0)
                right=(i==l-1 or flowerbed[i+1]==0)
                if left and right:
                    t+=1
                    i+=2
                else:
                    i+=1
        if t>=n:
            return True
        else: 
            return False
