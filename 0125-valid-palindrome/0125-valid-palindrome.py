class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch

        return new == new[::-1]