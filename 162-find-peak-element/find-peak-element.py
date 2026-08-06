class Solution(object):
    def findPeakElement(self, nums):
        n = len(nums)

        for i in range(n-1):

            if nums[i] > nums[i+1]:
                return i
        return n -1

object = Solution()
print(object.findPeakElement)