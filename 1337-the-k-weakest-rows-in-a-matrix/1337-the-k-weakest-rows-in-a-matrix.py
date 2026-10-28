class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        n=len(mat)
        m=len(mat[0])
        # arr=[[0]*2 for _ in range(n)]
        arr=[]
        ans=[]
        for i in range(n):
            arr.append([i,sum(mat[i])])
        # print(arr)
        arr.sort(key=lambda x:x[1])
        # print(arr)
        for j in range(k):
            ans.append(arr[j][0])
        return ans
            

