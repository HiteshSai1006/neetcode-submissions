class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums =  sorted(nums)
        ans=[]
        i=0
        j=i+1
        k = len(nums)-1

        for i in range(k-1):
            j=i+1
            k=len(nums)-1
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                if total==0:
                    if sorted([nums[i],nums[j],nums[k]]) not in ans:
                        ans.append(sorted([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1

                elif total >0:
                    k=k-1
                elif total <0:
                    j=j+1
        return ans
                


        