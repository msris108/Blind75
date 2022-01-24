class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        d = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }
        
        for i in s:
            if i in d:
                if stack: 
                    top = stack.pop()
                    if top != d[i]:
                        return False
                else:
                    return False
            else:
                stack.append(i)
                
        return False if stack else True