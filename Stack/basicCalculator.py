"""
224. Basic Calculator

Given a string s representing a valid expression,
implement a basic calculator to evaluate it,
and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

"""

class Solution:
    def calculate(self, s: str) -> int:
      # iterate the expression string in reverse order one character at a time
      # once we encounter a character which is not a digit, we push the operand onto the stack
      # when we encounter an opening (, this mean justs an expression just ended
      # do this until we get the final result

      numbersStack = []
      operandsStack = []

      currNumber = "0"
      currOperand = "+"

      result = 0

      for i in range(len(s)):
         char = s[i]

         if char.isdigit():
            currNumber += char

         elif char in ["+", "-"]:
            # before we replace our current operand, calculate previous number and put it into the result
            if currOperand == "-":
               result += -1 * int(currNumber)
            else:
               result += int(currNumber)

            # reset both
            currNumber = "0"
            currOperand = char

         elif char == "(":
            numbersStack.append(result)
            operandsStack.append(currOperand)

            result = 0
            currOperand = "+"
            currNumber = "0"

         elif char == ")":
            if currOperand == "-":
               result += -1 * (int(currNumber))
            else:
               result += int(currNumber)

            # take out previous context
            prevNum = numbersStack.pop() if numbersStack else "0"
            prevOp = operandsStack.pop() if operandsStack else "+"

            # update the new result
            if prevOp == "-":
               result = -1 * result

            result = prevNum + result

            # reset
            currNumber = "0"
            currOperand = "+"

      # left over
      if currNumber: result += -1 * (int(currNumber)) if currOperand == "-" else int(currNumber)

      return result

# O(N) time, where N is the length of the string
# O(N) space, for the stack used
