class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        h={}
        n=len(nums)
        curr = nums[0]

        for i in range(n):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                return nums[i]
            i +=1
        
        
        