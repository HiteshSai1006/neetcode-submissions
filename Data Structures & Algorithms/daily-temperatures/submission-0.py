class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        temp = temperatures
        n = len(temp)
        ans = [0] * n

        for i,t in enumerate(temp):
            while stack and stack[-1][0] < t:
                stack_t,stack_i = stack.pop()
                ans[stack_i] = i-stack_i
            stack.append((t,i))

        return ans
            


            
        