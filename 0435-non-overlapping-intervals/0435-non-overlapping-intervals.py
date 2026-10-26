class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        n=len(intervals)
        intervals.sort(key=lambda x: x[1])
        count=0
        prev=intervals[0][1]
        for i in range(1,n):
            if prev<=intervals[i][0]:
                prev=intervals[i][1]
            else:
                count+=1
        return count
