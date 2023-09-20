"""
212. Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.
"""

class TrieNode:
    def __init__(self):
        self.children = {}  # map a char : TrieNode
        self.isWord = False # lets us know if we are at the end of the word

    def addWord(self, word):
        current = self      # set the pointer to the root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]  # update the pointer
        current.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        # build our trie prefix tree
        for w in words:
            root.addWord(w)

        rows, cols = len(board), len(board[0])
        result, visited = set(), set() # result is the set of words

        def DFS(row, col, currentNode, word):
            #base cases
            if (row < 0 or col < 0 or
                row == rows or col == cols or
                (row,col) in visited or
                board[row][col] not in currentNode.children):
                return # out of bounds

            visited.add( (row,col) )
            currentNode = currentNode.children[board[row][col]] # update our node
            word += board[row][col] # add the current char to our word
            if currentNode.isWord:
                result.add(word)

            DFS(row - 1, col, currentNode, word)
            DFS(row + 1, col, currentNode, word)
            DFS(row, col - 1, currentNode, word)
            DFS(row, col + 1, currentNode, word)

            # remove because we are backtracking
            visited.remove( (row,col) )

        for row in range(rows):
            for col in range(cols):
                DFS(row, col, root, "")

        return list(result)
