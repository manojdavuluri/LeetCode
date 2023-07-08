class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []
        
        closetoOpen = {"}":"{","]":"[",")":"("}
        
        for i in s:        
            if i in closetoOpen:
                if myStack and myStack[-1] == closetoOpen[i]:
                    myStack.pop()
                else:
                    return False
            else:
                myStack.append(i)
                
        return True if not myStack else False