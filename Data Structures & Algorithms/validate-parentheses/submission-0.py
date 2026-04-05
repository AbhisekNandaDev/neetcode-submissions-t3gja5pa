class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        matching = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in matching:                          # closing bracket
                if not res or res[-1] != matching[i]:
                    return False
                res.pop()
            else:                                      # opening bracket
                res.append(i)
        
        return len(res) == 0