"""
150. Evaluate Reverse Polish Notation
You are given an array of strings tokens that represent an arithmetic expression in a
reverse polish notation. Evaluate the expression. Return an integer that represents the value of the expression.
Note that:
The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
      stack = []
      for character in tokens:
         if character == "+":
            stack.append(stack.pop() + stack.pop())
         elif character == "-":
            x, y = stack.pop(), stack.pop()
            stack.append(y - x)
         elif character == "*":
            stack.append(stack.pop() * stack.pop())
         elif character == "/":
            x, y = stack.pop(), stack.pop()
            stack.append(int(y / x))                # converting to integer allows for rounding to zero to occur
         else:
            stack.append(int(character))
      return stack[0]
