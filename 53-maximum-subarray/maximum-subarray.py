class Solution(object):
    def maxSubArray(self, nums):
        current_sum =nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])

            max_sum = max(current_sum , max_sum)
    
        return max_sum

object = Solution()
print(object.maxSubArray)