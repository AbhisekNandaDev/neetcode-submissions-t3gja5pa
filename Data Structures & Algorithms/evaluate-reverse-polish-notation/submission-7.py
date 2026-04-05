class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        stack=[]
        for i in tokens:
            if i == "+":
                val1=stack.pop()
                val2=stack.pop()

                stack.append(int(val2)+int(val1))

            elif i == "-":
                val1=stack.pop()
                val2=stack.pop()

                stack.append(int(val2)-int(val1))

            elif i == "*":
                val1=stack.pop()
                val2=stack.pop()

                stack.append(int(val2) * int(val1))

            elif i == "/":
                val1=stack.pop()
                val2=stack.pop()

                stack.append(int(val2) / int(val1))

            else:
                stack.append(i)

        return int(stack[-1])