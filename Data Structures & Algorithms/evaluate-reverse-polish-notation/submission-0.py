class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = {"+", "-", "*", "/"}
        stack = []

        for tok in tokens:

            if tok not in operators:
                stack.append(int(tok))
            
            else:
                b = stack.pop()
                a = stack.pop()

                if tok == "+":
                    result = a + b
                elif tok == "-":
                    result = a - b
                elif tok == "*":
                    result = a * b
                elif tok == "/":
                    result = int(a / b)
            
                stack.append(result)

        return stack[0]
                
        