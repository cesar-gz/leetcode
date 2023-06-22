"""
3. Find a Celebrity

Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know them but they do not know any of them.

Goal: You want to find out who the celebrity is or verify that there is not one.

Output: The number associated with the celebrity, or -1 if no celebrity present.

The only thing you are allowed to do is to ask questions like:

"Hi, A. Do you know B?" to get information of whether A knows B.
You need to find the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function knows(a, b)-->bool which tells you whether A knows B.

Implement a function findCelebrity(n)-->int, your function should minimize the number of calls to knows(a, b).
"""

"""
plan:
  1) create a stack and push elements o to n-1 onto the stack
  2) create two variables, left and right
  3) pop the first two elements into left and right respectively
  4) while the stack has individuals on it:
      a) if left knows right, left cannot be a celebrity
          i) pop the next elem into left
          ii) refer to right as a potential celebrity
      b) if left does not know right, right cannot be a celebrity
          i) pop the next elem into right
          ii) refer to left as a potential celebrity
  5) the potential celebrity reference is the most valid individual
      a) if valid return celebrity, else return -1

"""

def findCelebrity(n: int) -> int:
    if n < 2:
        # base case where there is 1 or less people
        return -1

    stack = []

    #put all people in the stack
    for i in range(n):
        stack.append(i)

    left = stack.pop
    right = stack.pop

    # if left knows right, then make right the potential celeb, otherwise make left the potential celeb
    potentialCeleb = left if not knows(left,right) else right

    while len(stack) > 0:
        # if left knows right
        if knows(left,right):
            potentialCeleb = right
            left = stack.pop()
        else:
            potentialCeleb = left
            right = stack.pop()

    # double check the potential celebrity
    for i in range(n):
        if i != potentialCeleb and ( not knows(i, potentialCeleb) or knows(potentialCeleb, i) ):
            return -1

    return potentialCeleb

# time complexity O(n), where n is the number of API calls to knows
# space complexity O(n), for the stack that held each person in n
