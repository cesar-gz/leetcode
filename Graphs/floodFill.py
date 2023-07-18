"""
733. Flood Fill

An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color.
You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel,
plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel,
plus any pixels connected 4-directionally to those pixels (also with the same color), and so on.
Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.
"""

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Check if our starting point color needs to be changed: If color is as intended return the image,
        #  other wise then continue
        if image[sr][sc] == color:
            return image

        # store our starting point color in a variable
        m, n, origColor = len(image), len(image[0]), image[sr][sc]

        # using a DFS call, we check its 4 directional neighbors, replacing those that the had the original
        # color, then shift columns
        def DFS(i, j):
            # check if neighbor is in bounds and is the same as the origColor, if it isn't, then return
            if i < 0 or i > m - 1 or j < 0  or j > n - 1 or image[i][j] != origColor:
                return

            image[i][j] = color
            DFS(i + 1, j)
            DFS(i - 1, j)
            DFS(i, j + 1)
            DFS(i, j - 1)

        DFS(sr, sc)
        return image
    # Time O(N) where N is the number of pixels in the image
    # Space O(N) where N is the size of the recursive call stack
