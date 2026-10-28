class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in sorted(set(s), key=s.count, reverse=True):
            ans += i * s.count(i)

        return ans