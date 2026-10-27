class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        n=len(boxTypes)
        boxTypes.sort(key=lambda x:-x[1])
        c=0
        for i in range(n):
            if truckSize == 0:
                break
            if truckSize>=boxTypes[i][0]:
                c+=(boxTypes[i][0]*boxTypes[i][1])
                truckSize-=boxTypes[i][0]
            elif truckSize>0:
                c+=(truckSize*boxTypes[i][1])
                truckSize-=truckSize
        return c

                
            
