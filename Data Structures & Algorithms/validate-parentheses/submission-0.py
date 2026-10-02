class Solution:
    def isValid(self, s: str) -> bool:

        operators={
            "]":"[",
            "}":"{",
            ")":"("
        }

        stack = []

        for char in s:

            if char not in operators:
                stack.append(char)
            
            else:
                if len(stack) == 0:
                    return False
                    # ie. s = }

                if stack[-1] != operators[char]:
                    return False
                
                stack.pop()
    
        return len(stack) == 0
        