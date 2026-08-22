class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n=len(nums)
        if n<1:
            return 0
        elif n ==1:
            return 1
        count = 1
        max_count=1
        diff= nums[0]
        for i in range(1,len(nums)):
            diff = nums[i] - nums[i-1]
            if diff == 0:
                continue
            elif diff == 1:
                count +=1
            else:
                count = 1
            max_count = max(count,max_count)
        return max_count
        


        