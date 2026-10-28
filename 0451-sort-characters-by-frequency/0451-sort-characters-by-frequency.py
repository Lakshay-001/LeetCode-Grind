class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # ans = ""
        # for i in sorted(set(s), key=s.count, reverse=True):
        #     ans += i * s.count(i)

        # return ans
        arr = []
        for i in s:
            found = False
            for j in arr:
                if j[0] == i:
                    found = True
                    break
            if not found:
                arr.append([i, s.count(i)])
        arr.sort(key=lambda x: x[1], reverse=True)
        ans = ""
        for i in arr:
            ans += i[0] * i[1]

        return ans