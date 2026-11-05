class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        def solve(i, arr, s):
            if s == target:
                ans.append(arr[:])
                return
            if s > target:
                return
            if i == len(candidates):
                return
            arr.append(candidates[i])
            solve(i, arr, s + candidates[i])
            arr.pop()
            solve(i + 1, arr, s)
        solve(0, [], 0)
        return ans