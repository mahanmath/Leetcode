class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if(tokens[i] not in ['+', '-', '*', '/']):
                stack.append(int(tokens[i]))
            else:
                op = tokens[i]
                b = stack.pop()
                a = stack.pop()
                
                if(op == '+'):
                    stack.append(a + b)
                elif(op == '-'):
                    stack.append(a - b)
                elif(op == '*'):
                    stack.append(a * b)
                else:
                    stack.append(int(a/b))
                    
        return(stack[0])
