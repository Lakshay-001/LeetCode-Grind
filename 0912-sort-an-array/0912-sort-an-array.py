# class Solution(object):
#     def sortArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         def part(nums,lo,hi):
#             p=nums[hi]
#             i=lo-1
#             for j in range(lo,hi+1):
#                 if nums[j]<=p:
#                     i+=1
#                     nums[i],nums[j]=nums[j],nums[i]
#             return i
#         def quick(nums,lo,hi):
#             if lo>=hi:
#                 return
#             l=part(nums,lo,hi)
#             quick(nums,lo,l-1)
#             quick(nums,l+1,hi)
#         quick(nums,0,len(nums)-1)
#         return nums
class Solution(object):
    def sortArray(self, nums):
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        ans = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1

        return ans + left[i:] + right[j:]