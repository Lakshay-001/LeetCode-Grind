class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        d={}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        freq = list(d.values())
        freq.sort(reverse=True)

        count = 0
        ans = 0
        n = len(arr)

        for i in freq:
            count += i
            ans += 1

            if count >= n // 2:
                break

        return ans