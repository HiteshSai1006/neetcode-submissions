class Solution: 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h={}
        for i in range(len(nums)):
            if nums[i] not in h:
                h[nums[i]] = 1
            else:
                h[nums[i]] +=1


        ans=[]
        for i in range(k):
            max_key = max(h,key=h.get)
            ans.append(max_key)
            h.pop(max_key)
        return ans