class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1

        if target == nums[0]:
            return l 
        elif target > nums[0]:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            else:
                return -1
        elif target < nums[0]:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i
            else:
                return -1