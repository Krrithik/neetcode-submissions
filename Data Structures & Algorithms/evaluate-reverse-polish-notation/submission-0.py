class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators_list = ["+", "-", "*", "/"]
        stack = []
        
        for token in tokens:
            if token not in operators_list:
                stack.append(int(token))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                match token:
                    case "+":
                        stack.append(num1 + num2)
                    case "-":
                        stack.append(num1 - num2)
                    case "*":
                        stack.append(num1 * num2)
                    case "/":
                        # Truncate toward zero for division
                        stack.append(int(num1 / num2))
                        
        return stack.pop()