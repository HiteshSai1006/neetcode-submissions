class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        #left to right prefix sum
        prefixsum = [1] * n
        prefixsum[0] = nums[0]
        for i in range(1,len(nums)):
            prefixsum[i] = prefixsum[i-1] * nums[i]

        #right to left prefix sum
        suffixsum = [1] * n
        suffixsum[n-1] = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            suffixsum[i] = suffixsum[i+1] * nums[i]

        #excepting nums[i]
        result[0] = suffixsum[1]
        result[n-1] = prefixsum[n-2]
        for i in range(1,len(nums)-1):
            result[i] = prefixsum[i-1]*suffixsum[i+1]

        return result


        