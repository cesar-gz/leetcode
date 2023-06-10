"""
397. Integer Replacement
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

"""
class Solution:
    def integerReplacement(self, n):
        # base case
        if n <= 1:
            return 0
        operationCount = 0
        while n != 1:
          if n % 2 == 0:
              # then it is a even number, divide n by 2, increment count by 1
              n, operationCount = n/2, operationCount + 1
          elif n == 3:
              n, operationCount = n-1, operationCount + 1
          else:
              # then it is a odd number
              if ((n-1)/2) % 2 == 0:
                  # the resulting n is even
                  n, operationCount = n-1, operationCount + 1
              else:
                  # the resulting n is odd
                  n, operationCount = n+1, operationCount + 1
        return operationCount
