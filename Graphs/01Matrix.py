"""
542. 01 Matrix
Given an m x n binary matrix, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
"""

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        seen = set()
        q = deque()

        # queue up all the zero values
        for r in range(rows):
          for c in range(cols):
            if mat[r][c] == 0:
                q.append( (r,c) )
                seen.add( (r,c) )

        # traverse level order wise, and for each level update the distance
        coords = [(0,1), (1,0), (0,-1), (-1, 0)]
        distance = 1

        while q:
           for _ in range(len(q)):
              row, col = q.popleft()
              for rc, cc in coords:
                 r = row + rc
                 c = col + cc
                 # add element back to queue, also for the next level traversal
                 # in this way, those who are not reachable to any zero in the first attempt
                 # the next level will be checked, and the counter incremented
                 if r >= 0 and r < rows and c >= 0 and c < cols and (r,c) not in seen:
                    mat[r][c] = distance
                    q.append( (r,c) )
                    seen.add( (r,c) )
           distance += 1
        return mat
    # O(N*M) Time to view each item in the matrix
    # O(N*M) Space we need to store each item in the queue
