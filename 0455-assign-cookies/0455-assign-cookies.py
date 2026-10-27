class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        c=0
        g.sort(reverse=True)
        s.sort(reverse=True)
        i=0
        j=0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                c += 1
                i += 1
                j += 1
            else:
                i += 1

        return c

        