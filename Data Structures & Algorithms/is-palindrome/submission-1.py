class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        s=s.lower()
        left=0
        right=n-1
        is_palindrome=True

        while left<right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] != s[right]:
                    is_palindrome = False
                    break
                left+=1
                right-=1
            
            elif s[left].isalnum()==False:
                left+=1
            elif s[right].isalnum() == False:
                right-=1
        return is_palindrome
        
            


        