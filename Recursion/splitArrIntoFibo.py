"""
842. Split Array into Fibonacci Sequence

You are given a string of digits num, such as "123456579". We can split it into a Fibonacci-like sequence [123, 456, 579].

Formally, a Fibonacci-like sequence is a list f of non-negative integers such that:

f.length >= 3

Note that when splitting the string into pieces, each piece must not have extra leading zeroes, except if the piece is the number 0 itself.

Return any Fibonacci-like sequence split from num, or return [] if it cannot be done.
"""

class Solution:
    def splitIntoFibonacci(self, num: str) -> list[int]:
        n = len(num)

        def fibo(position, result, n, finish):
            if position >= n:
                if len(result) > 2:
                    finish.append(result.copy()) # add to rhe result array of ot contains 3 or more elements
                return

            currentStr = ""
            for i in range(position, n):
                currentStr += num[i]

                if currentStr[0] == "0" and i != position:
                    continue # check if first number of more than one digit is equal to 0, we have to ignore leading zeros

                if int(currentStr) > (2**31):
                    break    # outside of the constraints of the problem

                if len(result) >= 2:
                    if int(currentStr) == int(result[-1]) + int(result[-2]):
                        result.append(currentStr)
                        fibo(i + 1, result, n, finish)
                        result.pop()  # check that each splitted number equals to previous two numbers
                else:
                    result.append(currentStr)
                    fibo(i + 1, result, n, finish)
                    result.pop()      # if current array has less than two numbers, we can add them to the arrayy
        finish, result = [], []
        fibo(0, result, n, finish)
        answer = []
        if len(finish) == 0 or finish == []:    # if input is empty, return empty
            return []
        for i in finish[0]:
            answer.append(int(i))
        return answer
