class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_volume=0
        left = 0
        right = n-1

        while left<right:
            height = min(heights[left],heights[right])
            distance = right-left
            volume = height*distance
            max_volume = max(volume,max_volume)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1

        return max_volume



        