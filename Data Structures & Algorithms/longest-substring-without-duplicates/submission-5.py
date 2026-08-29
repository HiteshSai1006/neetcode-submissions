class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n<1:
            return 0
        seen =set()
        l=0
        max_length = 1

        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l=l+1
            seen.add(s[r])
            count = r+1 - l
            max_length = max(count,max_length)

        return max_length

        