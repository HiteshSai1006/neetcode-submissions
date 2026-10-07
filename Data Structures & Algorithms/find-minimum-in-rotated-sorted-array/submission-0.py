class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        
        if nums[l] > nums[r]:
            #array rotated
            for i in range(r):
                if nums[i]>nums[i+1]:
                    return nums[i+1]
        else:
            return nums[l]
