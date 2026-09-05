class Solution:
    def isValid(self, s: str) -> bool:
        n=len(s)
        valid = False
        if n%2!=0:
            valid = False
            return valid
  
        open={"(" :")",
            "[" : "]",
            "{" : "}"
            }
        close ={")" : "(",
                "]" : "[",
                "}" : "{"
                }
        stack = []
        for i in range(n):
            if s[i] in open:
                stack.append(s[i])
    
            elif s[i] in close:
                if len(stack) == 0:
                    valid = False
                else:
                    a = stack.pop()
                    if a in open and open[a] == s[i]:
                        valid = True
                    else:
                        valid = False
                        break
        if len(stack)!=0:
            valid = False
        return valid
        