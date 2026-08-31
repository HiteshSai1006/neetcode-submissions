class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        h={}
        for i in range(len(s1)):
            h[s1[i]]= h.get(s1[i],0)+1
        s1=sorted(s1)
        l=0
        permutation = False
        n=len(s1)
        for r in range(len(s2)):
            if s2[r] in h:
                l=r
                r=l+n
                string = s2[l:r]
                string = sorted(string)
                if string == s1:
                    permutation = True
        return permutation


        