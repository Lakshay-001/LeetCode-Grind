class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        su = 0
        for ch in s:
            if ch == "(":
                stack.append(0)
            else:
                top = stack.pop()
                if top == 0:
                    val = 1
                else:
                    val = 2 * top
                if stack:
                    stack[-1] += val
                else:
                    su += val
        return su