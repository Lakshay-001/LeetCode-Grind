class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        arr = []
        for i in range(len(capacity)):
            arr.append(capacity[i] - rocks[i])
        arr.sort()
        ans = 0
        for i in range(len(arr)):
            if additionalRocks >= arr[i]:
                additionalRocks -= arr[i]
                ans += 1
            else:
                break

        return ans